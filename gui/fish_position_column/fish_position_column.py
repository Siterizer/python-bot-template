from tkinter import Label, LabelFrame

from gui.fish_position_column.components.positions import fish_position_column_position
from gui.fish_position_column.components.attributes import fish_position_column_attributes
from gui.fish_position_column.components.show_button import fish_position_column_show_button


def add_fish_position_column(app, config):
    fish_position_header = Label(app, text="Fish Position")
    fish_position_header.grid(row=0, column=0, pady=(3, 0))
    fish_position_column = LabelFrame(app)
    fish_position_column.grid(row=1, column=0, padx=(10, 0), pady=(0, 30))

    fish_position_column_position(fish_position_column, config)
    fish_position_column_attributes(fish_position_column, config)
    fish_position_column_show_button(app, fish_position_column, config)