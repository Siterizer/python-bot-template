from tkinter import LabelFrame, Button

from functools import partial


def fish_progress_column_show_button(app, fish_progress_column, config):
    fish_progress_column_show_container = LabelFrame(fish_progress_column)
    fish_progress_column_show_container.grid(row=4, column=0, pady=(5, 0))
    fish_progress_column_show_button = Button(fish_progress_column_show_container, text="Show progress position")
    fish_progress_column_show_button.configure(
        command=partial(
            app.popup_rectangle_window,
            fish_progress_column_show_button,
            config["fishing"]['fishing-progress']["x"],
            config["fishing"]['fishing-progress']["y"],
            config["fishing"]['fishing-progress']["width"],
            config["fishing"]['fishing-progress']["height"])
    )
    fish_progress_column_show_button.grid(row=4, column=0, padx=(34, 34), pady=(2, 4))