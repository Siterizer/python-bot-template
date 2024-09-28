import asyncio
import logging
import random
import string
import threading
import tkinter as tk
from functools import partial

from functionality.fishing_loop import fishing_loop
from utils.config import get_config, save_data
from utils.global_variables import ICON_PATH
from functools import partial
from wrappers.logging_wrapper import log_level, info
from gui.fish_position_column.fish_position_column import add_fish_position_column
from gui.fishing_progress_column.fishing_status_column import add_fish_progress_column
from gui.bottom_buttons import add_bottom_buttons


class FishingBot(tk.Tk):
    def __init__(self):
        super().__init__()

        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", partial(self.on_closing))
        self.iconbitmap(ICON_PATH)
        self.title("".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)))

        self.continue_fishing = False
        self.fishing_coro = None
        self.asyncio_event_loop = asyncio.get_event_loop()
        self.config = get_config()

        print(self.config["log_lvl"])
        logging.getLogger().setLevel(log_level.get(self.config["log_lvl"], "INFO"))

        add_fish_position_column(self, self.config)
        add_fish_progress_column(self, self.config)
        add_bottom_buttons(self)

        #self.asyncio_event_loop.set_debug(True)
        threading.Thread(daemon=True, target=self.asyncio_event_loop.run_forever).start()

    def popup_rectangle_window(self, button, x, y, width, height):
        window = tk.Toplevel()
        window.resizable(False, False)
        window.attributes("-fullscreen", True)
        window.wm_attributes("-transparentcolor", window["bg"])
        window.attributes("-topmost", True)
        canvas = tk.Canvas(window, width=10000, height=10000)
        canvas.create_rectangle(
            x.get(),
            y.get(),
            x.get() + width.get(),
            y.get() + height.get(),
            outline="green",
            width=5,
        )
        canvas.pack()
        button.configure(command=partial(self.destroy_rectangle_window, window, button, x, y, width, height))

    def destroy_rectangle_window(self, window, button, x, y, width, height):
        window.destroy()
        button.configure(command=partial(self.popup_rectangle_window, button, x, y, width, height))

    #no idea how to make it in other way
    def popup_rectangle_window_with_red_middle(self, button, x, y, width, height):
        window = tk.Toplevel()
        window.resizable(False, False)
        window.attributes("-fullscreen", True)
        window.wm_attributes("-transparentcolor", window["bg"])
        window.attributes("-topmost", True)
        canvas = tk.Canvas(window, width=10000, height=10000)
        canvas.create_rectangle(
            x.get(),
            y.get(),
            x.get() + width.get(),
            y.get() + height.get(),
            outline="green",
            width=5,
        )
        canvas.create_rectangle(
            x.get() + (width.get())/2,
            y.get(),
            x.get() + (width.get())/2,
            y.get() + 10,
            outline="red",
            width=10,
        )
        canvas.pack()
        button.configure(command=partial(self.destroy_rectangle_window_with_red_middle, window, button, x, y, width, height))

    def destroy_rectangle_window_with_red_middle(self, window, button, x, y, width, height):
        window.destroy()
        button.configure(command=partial(self.popup_rectangle_window_with_red_middle, button, x, y, width, height))

    def on_closing(self):
        save_data(self.config)
        self.destroy()

    def save_data(self):
        save_data(self.config)

    def changeFishingState(self, button):
        self.continue_fishing = not self.continue_fishing
        if self.continue_fishing:
            info("Starting fishing minigame")
            button.configure(text="Stop fishing")
            button.configure(command=partial(self.changeFishingState, button))
            return
        info("Stopping fishing minigame")
        button.configure(text="Start fishing")

        try:
            task = [task for task in asyncio.all_tasks(self.asyncio_event_loop) if task.get_name() == "fishing_loop"]
           
            if task:
                task = task.pop()
                self.asyncio_event_loop.call_soon_threadsafe(task.cancel)
        except asyncio.CancelledError:
            pass

        button.configure(command=partial(self.start_fishing, button))

    def start_fishing(self, button):
        self.changeFishingState(button)
        self.fishing_coro = self.asyncio_event_loop.call_soon_threadsafe(self.do_create_task)

    def do_create_task(self):
        self.asyncio_event_loop.create_task(fishing_loop(self.config), name="fishing_loop")


if __name__ == "__main__":
    app = FishingBot()
    app.mainloop()
