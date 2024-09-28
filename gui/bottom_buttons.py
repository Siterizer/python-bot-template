from tkinter import Button, LabelFrame
from functools import partial



def add_bottom_buttons(app):
    buttons_container = LabelFrame(app)
    buttons_container.grid(row=3, columnspan=3, padx=(10, 0), pady=(15, 0))

    add_start_fishing_button(app, buttons_container)
    add_save_data_button(app, buttons_container)




def add_start_fishing_button(app, cointainer):
    start_fishing_button = Button(
        cointainer, text="Start fishing", font=18
    )
    start_fishing_button.configure(command=partial(app.start_fishing, start_fishing_button))
    start_fishing_button.grid(row=0, column=0, padx=(5))

def add_save_data_button(app, cointainer):
    save_data_button = Button(
        cointainer, text="Save data", font=18
    )
    save_data_button.configure(command=partial(app.save_data))
    save_data_button.grid(row=0, column=1, padx=(5))