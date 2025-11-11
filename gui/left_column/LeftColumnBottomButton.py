from tkinter import LabelFrame, Button
import tkinter as tk

from functools import partial
from utils.config import get_config

class LeftColumnBottomButton:
    def __init__(self, column):
        config = get_config()
        
        button_container = LabelFrame(column)
        button_container.grid(row=4, column=0, pady=(5, 0))
        button = Button(button_container, text="Show fishing position")
        button.configure(
            command=partial(self.popup_window,
                button,
                config["fishing"]['fish-position']["x"],
                config["fishing"]['fish-position']["y"],
                config["fishing"]['fish-position']["width"],
                config["fishing"]['fish-position']["height"]))
        button.grid(row=4, column=0, padx=(34, 34), pady=(2, 4))

    def popup_window(self, button, x, y, width, height):
        window = tk.Toplevel()
        window.resizable(False, False)
        window.attributes("-fullscreen", True)
        window.wm_attributes("-transparentcolor", window["bg"])
        window.attributes("-topmost", True)
        canvas = tk.Canvas(window, width=10000, height=10000)
        canvas.create_rectangle(x.get(), y.get(), x.get() + width.get(), y.get() + height.get(), outline="green", width=5)
        canvas.create_rectangle(x.get() + (width.get()) / 2, y.get(), x.get() + (width.get()) / 2, y.get() + 10, outline="red", width=10)
        canvas.pack()
        button.configure(command=partial(self.destroy_window, window, button, x, y, width, height))

    def destroy_window(self, window, button, x, y, width, height):
        window.destroy()
        button.configure(command=partial(self.popup_window, button, x, y, width, height))