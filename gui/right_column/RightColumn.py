from tkinter import Label, LabelFrame, Scale, Entry, HORIZONTAL

from gui.right_column.RightColumnBottomButton import RightColumnBottomButton

class RightColumn:
    def __init__(self, app):
        self.config = app.config

        header = Label(app, text="Fish Progress")
        header.grid(row=0, column=1, pady=(3, 0))
        right_column = LabelFrame(app)
        right_column.grid(row=1, column=1, padx=(10, 0), pady=(0, 30))

        self.position_slider(right_column)
        self.attributes_slider(right_column)
        RightColumnBottomButton(right_column)

    def position_slider(self, right_column):
        header = Label(right_column, text="Progress position (px)")
        header.grid(row=0, column=0)
        container = LabelFrame(right_column)
        container.grid(row=1, column=0, padx=(10))
        x_container = Label(container, height=1)
        x_container.grid(row=0, column=0, padx=(20, 19))
        x_text = Label(x_container, text="X:")
        x_text.grid(row=0, column=0, pady=(20, 0))
        x_scale = Scale(x_container, from_=0, to=5120, orient=HORIZONTAL, variable=self.config["fishing"]["fishing-progress"]["x"],)
        x_scale.grid(row=0, column=1)
        x_entry = Entry(x_container, width=4, textvariable=self.config["fishing"]["fishing-progress"]["x"])
        x_entry.grid(row=0, column=2, pady=(20, 0))

        y_container = Label(container, height=1)
        y_container.grid(row=1, column=0)
        y_text = Label(y_container, text="Y:")
        y_text.grid(row=0, column=0, pady=(20, 0))
        y_scale = Scale(y_container, from_=0, to=2160, orient=HORIZONTAL, variable=self.config["fishing"]["fishing-progress"]["y"])
        y_scale.grid(row=0, column=1)
        y_entry = Entry(y_container, width=4, textvariable=self.config["fishing"]["fishing-progress"]["y"])
        y_entry.grid(row=0, column=2, pady=(20, 0))

    def attributes_slider(self, right_column):
        header = Label(right_column, text="Progress attributes (px)")
        header.grid(row=2, column=0)
        container = LabelFrame(right_column)
        container.grid(row=3, column=0, padx=(10))
        width_container = Label(container, height=1)
        width_container.grid(row=0, column=0, padx=(5))
        width_text = Label(width_container, text="Width:")
        width_text.grid(row=0, column=0, pady=(20, 0))
        width_scale = Scale(width_container, from_=0,to=5120, orient=HORIZONTAL, variable=self.config["fishing"]['fishing-progress']["width"])
        width_scale.grid(row=0, column=1)
        width_entry = Entry(width_container, width=4, textvariable=self.config["fishing"]['fishing-progress']["width"])
        width_entry.grid(row=0, column=2, pady=(20, 0))
        
        height_container = Label(container, height=1)
        height_container.grid(row=1, column=0, padx=(5))
        height_text = Label(height_container, text="Height:")
        height_text.grid(row=0, column=0, pady=(20, 0))
        height_scale = Scale( height_container, from_=0, to=2160, orient=HORIZONTAL, variable=self.config["fishing"]['fishing-progress']["height"])
        height_scale.grid(row=0, column=1)
        height_entry = Entry(height_container, width=4, textvariable=self.config["fishing"]['fishing-progress']["height"])
        height_entry.grid(row=0, column=2, pady=(20, 0))