from tkinter import LabelFrame, Button, IntVar

from functools import partial


def fish_position_column_show_button(app, fish_position_column, config):
    fish_position_column_show_container = LabelFrame(fish_position_column)
    fish_position_column_show_container.grid(row=4, column=0, pady=(5, 0))
    fish_position_column_show_button = Button(fish_position_column_show_container, text="Show fishing position")
    fish_position_column_show_button.configure(
        command=partial(app.popup_rectangle_window_with_red_middle,
            fish_position_column_show_button,
            config["fishing"]['fish-position']["x"],
            config["fishing"]['fish-position']["y"],
            config["fishing"]['fish-position']["width"],
            config["fishing"]['fish-position']["height"]))
    fish_position_column_show_button.grid(row=4, column=0, padx=(34, 34), pady=(2, 4))

