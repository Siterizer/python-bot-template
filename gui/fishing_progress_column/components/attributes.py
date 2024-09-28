from tkinter import Label, LabelFrame, Scale, Entry, HORIZONTAL


def fish_progress_column_attributes(fish_status_column, config):
    fish_progress_column_attributes_header = Label(fish_status_column, text="Progress attributes (px)")
    fish_progress_column_attributes_header.grid(row=2, column=0)
    fish_progress_column_attributes_container = LabelFrame(fish_status_column)
    fish_progress_column_attributes_container.grid(row=3, column=0, padx=(10))
    fish_progress_column_attributes_width_container = Label(fish_progress_column_attributes_container, height=1)
    fish_progress_column_attributes_width_container.grid(row=0, column=0, padx=(5))
    fish_progress_column_attributes_width_text = Label(fish_progress_column_attributes_width_container, text="Width:")
    fish_progress_column_attributes_width_text.grid(row=0, column=0, pady=(20, 0))
    fish_progress_column_attributes_width_scale = Scale(
        fish_progress_column_attributes_width_container,
        from_=0,
        to=5120,
        orient=HORIZONTAL,
        variable=config["fishing"]['fishing-progress']["width"],
    )
    fish_progress_column_attributes_width_scale.grid(row=0, column=1)
    fish_progress_column_attributes_width_entry = Entry(
        fish_progress_column_attributes_width_container,
        width=4,
        textvariable=config["fishing"]['fishing-progress']["width"],
    )
    fish_progress_column_attributes_width_entry.grid(row=0, column=2, pady=(20, 0))
    fish_progress_column_attributes_height_container = Label(fish_progress_column_attributes_container, height=1)
    fish_progress_column_attributes_height_container.grid(row=1, column=0, padx=(5))
    fish_progress_column_attributes_height_text = Label(fish_progress_column_attributes_height_container, text="Height:")
    fish_progress_column_attributes_height_text.grid(row=0, column=0, pady=(20, 0))
    fish_progress_column_attributes_height_scale = Scale(
        fish_progress_column_attributes_height_container,
        from_=0,
        to=2160,
        orient=HORIZONTAL,
        variable=config["fishing"]['fishing-progress']["height"],
    )
    fish_progress_column_attributes_height_scale.grid(row=0, column=1)
    fish_progress_column_attributes_height_entry = Entry(
        fish_progress_column_attributes_height_container,
        width=4,
        textvariable=config["fishing"]['fishing-progress']["height"],
    )
    fish_progress_column_attributes_height_entry.grid(row=0, column=2, pady=(20, 0))