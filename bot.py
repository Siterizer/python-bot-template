import asyncio
import logging
import random
import string
import threading
import tkinter as tk
from functools import partial

from utils.config import get_config, save_data
from utils.global_variables import ICON_PATH
from functools import partial


class FishingBot(tk.Tk):
    def __init__(self):
        super().__init__()

        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", partial(self.on_closing))
        self.iconbitmap(ICON_PATH)
        self.title("".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)))

        self.asyncio_event_loop = asyncio.get_event_loop()
        self.config = get_config()

        # self.asyncio_event_loop.set_debug(True)
        threading.Thread(daemon=True, target=self.asyncio_event_loop.run_forever).start()

    def on_closing(self):
        save_data(self.config)
        self.destroy()

if __name__ == "__main__":
    app = FishingBot()
    app.mainloop()
