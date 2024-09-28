from tkinter import Label, LabelFrame

from gui.fishing_progress_column.components.positions import fish_progress_column_position
from gui.fishing_progress_column.components.attributes import fish_progress_column_attributes
from gui.fishing_progress_column.components.show_button import fish_progress_column_show_button

def add_fish_progress_column(app, config):
    fish_progress_header = Label(app, text="Fish Progress")
    fish_progress_header.grid(row=0, column=1, pady=(3, 0))
    fish_progress_column = LabelFrame(app)
    fish_progress_column.grid(row=1, column=1, padx=(10, 0), pady=(0, 30))

    fish_progress_column_position(fish_progress_column, config)
    fish_progress_column_attributes(fish_progress_column, config)
    fish_progress_column_show_button(app, fish_progress_column, config)