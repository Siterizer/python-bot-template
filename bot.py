import logging
import random
import string
import tkinter as tk
from functools import partial

from utils.config import get_config, save_data
from utils.global_variables import ICON_PATH
from wrappers.logging_wrapper import log_level
from gui.fish_position_column.fish_position_column import add_fish_position_column
from gui.fishing_progress_column.fishing_status_column import add_fish_progress_column
from gui.BottomButtons import BottomButtons


class FishingBot(tk.Tk):
    def __init__(self):
        super().__init__()

        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", partial(self.on_closing))
        self.iconbitmap(ICON_PATH)
        self.title(
            "".join(
                random.choice(string.ascii_uppercase + string.digits) for _ in range(10)
            )
        )

        self.config = get_config()

        print(self.config["log_lvl"])
        logging.getLogger().setLevel(log_level.get(self.config["log_lvl"], "INFO"))

        add_fish_position_column(self, self.config)
        add_fish_progress_column(self, self.config)
        BottomButtons(self)

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
        button.configure(
            command=partial(
                self.destroy_rectangle_window, window, button, x, y, width, height
            )
        )

    def destroy_rectangle_window(self, window, button, x, y, width, height):
        window.destroy()
        button.configure(
            command=partial(self.popup_rectangle_window, button, x, y, width, height)
        )

    # no idea how to make it in other way
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
            x.get() + (width.get()) / 2,
            y.get(),
            x.get() + (width.get()) / 2,
            y.get() + 10,
            outline="red",
            width=10,
        )
        canvas.pack()
        button.configure(
            command=partial(
                self.destroy_rectangle_window_with_red_middle,
                window,
                button,
                x,
                y,
                width,
                height,
            )
        )

    def destroy_rectangle_window_with_red_middle(
        self, window, button, x, y, width, height
    ):
        window.destroy()
        button.configure(
            command=partial(
                self.popup_rectangle_window_with_red_middle, button, x, y, width, height
            )
        )

    def on_closing(self):
        save_data()
        self.destroy()


if __name__ == "__main__":
    app = FishingBot()
    app.mainloop()
