from yaml import safe_load, dump
from tkinter import IntVar
from utils.global_variables import CONFIG_PATH
from numpy import random

def get_config():
    config = safe_load(open(CONFIG_PATH))

    return {
        "fishing": {
            "x": IntVar(value=config["fishing"]["x"]),
            "y": IntVar(value=config["fishing"]["y"])
        },
        "log_lvl": config["log_lvl"],
    }


def save_data(config):
    d = {
        "fishing": {
            "x": config["fishing"]["x"].get(),
            "y": config["fishing"]["y"].get()
        },
        "log_lvl": config["log_lvl"],
    }
    with open(CONFIG_PATH, "w") as yaml_file:
        dump(d, yaml_file, sort_keys=False)


async def random_timeout(key):
    upper_limit = key["max"]
    lower_limit = key["min"]

    loc = (upper_limit + lower_limit) / 2
    scale = (upper_limit - lower_limit) / 4

    sample = random.normal(loc, scale)

    return round(min(max(sample, lower_limit), upper_limit), 2)