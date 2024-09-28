from tkinter import Label, LabelFrame, Scale, Entry, HORIZONTAL


def fish_progress_column_position(fishing_column, config):
    fish_progress_column_position_header = Label(fishing_column, text="Progress position (px)")
    fish_progress_column_position_header.grid(row=0, column=0)
    fish_progress_column_position_container = LabelFrame(fishing_column)
    fish_progress_column_position_container.grid(row=1, column=0, padx=(10))
    fish_progress_column_position_x_container = Label(fish_progress_column_position_container, height=1)
    fish_progress_column_position_x_container.grid(row=0, column=0, padx=(20, 19))
    fish_progress_column_position_x_text = Label(fish_progress_column_position_x_container, text="X:")
    fish_progress_column_position_x_text.grid(row=0, column=0, pady=(20, 0))
    fish_progress_column_position_x_scale = Scale(
        fish_progress_column_position_x_container,
        from_=0,
        to=5120,
        orient=HORIZONTAL,
        variable=config["fishing"]["fishing-progress"]["x"],
    )
    fish_progress_column_position_x_scale.grid(row=0, column=1)
    fish_progress_column_position_x_entry = Entry(
        fish_progress_column_position_x_container, width=4, textvariable=config["fishing"]["fishing-progress"]["x"]
    )
    fish_progress_column_position_x_entry.grid(row=0, column=2, pady=(20, 0))
    fish_progress_column_position_y_container = Label(fish_progress_column_position_container, height=1)
    fish_progress_column_position_y_container.grid(row=1, column=0)
    fish_progress_column_position_y_text = Label(fish_progress_column_position_y_container, text="Y:")
    fish_progress_column_position_y_text.grid(row=0, column=0, pady=(20, 0))
    fish_progress_column_position_y_scale = Scale(
        fish_progress_column_position_y_container,
        from_=0,
        to=2160,
        orient=HORIZONTAL,
        variable=config["fishing"]["fishing-progress"]["y"],
    )
    fish_progress_column_position_y_scale.grid(row=0, column=1)
    fish_progress_column_position_y_entry = Entry(
        fish_progress_column_position_y_container, width=4, textvariable=config["fishing"]["fishing-progress"]["y"]
    )
    fish_progress_column_position_y_entry.grid(row=0, column=2, pady=(20, 0))