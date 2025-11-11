from tkinter import LabelFrame, Button
import tkinter as tk

from functools import partial
from utils.config import get_config


class RightColumnBottomButton:
    def __init__(self, right_column):
        config = get_config()

        container = LabelFrame(right_column)
        container.grid(row=4, column=0, pady=(5, 0))
        button = Button(container, text="Show progress position")
        button.configure(
            command=partial(self.popup_window,
                button,
                config["fishing"]['fishing-progress']["x"],
                config["fishing"]['fishing-progress']["y"],
                config["fishing"]['fishing-progress']["width"],
                config["fishing"]['fishing-progress']["height"])
        )
        button.grid(row=4, column=0, padx=(34, 34), pady=(2, 4))

    def popup_window(self, button, x, y, width, height):
        window = tk.Toplevel()
        window.resizable(False, False)
        window.attributes("-fullscreen", True)
        window.wm_attributes("-transparentcolor", window["bg"])
        window.attributes("-topmost", True)
        canvas = tk.Canvas(window, width=10000, height=10000)
        canvas.create_rectangle(x.get(), y.get(), x.get() + width.get(), y.get() + height.get(), outline="green", width=5)
        canvas.pack()
        button.configure(command=partial(self.destroy_window, window, button, x, y, width, height))

    def destroy_window(self, window, button, x, y, width, height):
        window.destroy()
        button.configure(command=partial(self.popup_window, button, x, y, width, height))