import asyncio
from tkinter import Button, LabelFrame
from functools import partial
import threading

from wrappers.logging_wrapper import info
from functionality.fishing_loop import fishing_loop
from utils.config import save_data


class BottomButtons:
    def __init__(self, app):
        buttons_container = LabelFrame(app)
        buttons_container.grid(row=3, columnspan=3, padx=(10, 0), pady=(15, 0))

        self.continue_fishing = False
        self.fishing_coro = None
        self.config = app.config

        self.add_start_fishing_button(buttons_container)
        self.add_save_data_button(buttons_container)

    def add_start_fishing_button(self, cointainer):
        start_fishing_button = Button(cointainer, text="Start fishing", font=18)
        start_fishing_button.configure(
            command=partial(self.start_fishing, start_fishing_button)
        )
        start_fishing_button.grid(row=0, column=0, padx=(5))
        self.asyncio_event_loop = asyncio.get_event_loop()
        threading.Thread(
            daemon=True, target=self.asyncio_event_loop.run_forever
        ).start()

    def add_save_data_button(self, cointainer):
        save_data_button = Button(cointainer, text="Save data", font=18)
        save_data_button.configure(command=partial(save_data))
        save_data_button.grid(row=0, column=1, padx=(5))

    def change_fishing_state(self, button):
        self.continue_fishing = not self.continue_fishing
        if self.continue_fishing:
            info("Starting fishing minigame")
            button.configure(text="Stop fishing")
            button.configure(command=partial(self.change_fishing_state, button))
            return
        info("Stopping fishing minigame")
        button.configure(text="Start fishing")

        try:
            task = [
                task
                for task in asyncio.all_tasks(self.asyncio_event_loop)
                if task.get_name() == "fishing_loop"
            ]

            if task:
                task = task.pop()
                self.asyncio_event_loop.call_soon_threadsafe(task.cancel)
        except asyncio.CancelledError:
            pass

        button.configure(command=partial(self.start_fishing, button))

    def start_fishing(self, button):
        self.change_fishing_state(button)
        self.fishing_coro = self.asyncio_event_loop.call_soon_threadsafe(
            self.do_create_task
        )

    def do_create_task(self):
        self.asyncio_event_loop.create_task(
            fishing_loop(), name="fishing_loop"
        )
