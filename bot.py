import logging
import random
import string
import tkinter as tk
from functools import partial

from gui.left_column.LeftColumn import LeftColumn
from gui.right_column.RightColumn import RightColumn
from utils.config import get_config, save_data
from utils.global_variables import ICON_PATH
from wrappers.logging_wrapper import log_level
from gui.BottomButtons import BottomButtons


class FishingBot(tk.Tk):
    def __init__(self):
        super().__init__()

        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", partial(self.on_closing))
        self.iconbitmap(ICON_PATH)
        self.title("".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)))
        self.config = get_config()

        print(self.config["log_lvl"])
        logging.getLogger().setLevel(log_level.get(self.config["log_lvl"], "INFO"))

        LeftColumn(self)
        RightColumn(self)
        BottomButtons(self)

    def on_closing(self):
        save_data()
        self.destroy()


if __name__ == "__main__":
    app = FishingBot()
    app.mainloop()
