from yaml import safe_load, dump
from tkinter import IntVar
from utils.global_variables import CONFIG_PATH
from numpy import random

def get_config():
    config = safe_load(open(CONFIG_PATH))

    return {
        "fishing": {
            "check-area": {
            "x": IntVar(value=config["fishing"]["check-area"]["x"]),
            "y": IntVar(value=config["fishing"]["check-area"]["y"]),
            "width": IntVar(value=config["fishing"]["check-area"]["width"]),
            "height": IntVar(value=config["fishing"]["check-area"]["height"]),
            },
            "key-binds": {
                "block": config["fishing"]["key-binds"]["block"],
                "cast": config["fishing"]["key-binds"]["cast"],
                "drag-left": config["fishing"]["key-binds"]["drag-left"],
                "drag-right": config["fishing"]["key-binds"]["drag-right"],
            },
            "timeouts": {
                "loop": {
                    "min": config["fishing"]["timeouts"]["loop"]["min"],
                    "max": config["fishing"]["timeouts"]["loop"]["max"],
                },
                "notice-spam": {
                    "min": config["fishing"]["timeouts"]["notice-spam"]["min"],
                    "max": config["fishing"]["timeouts"]["notice-spam"]["max"],
                },
                "reeling": {
                    "min": config["fishing"]["timeouts"]["reeling"]["min"],
                    "max": config["fishing"]["timeouts"]["reeling"]["max"],
                },
                "reeling-pause": {
                    "min": config["fishing"]["timeouts"]["reeling-pause"]["min"],
                    "max": config["fishing"]["timeouts"]["reeling-pause"]["max"],
                },
                "recast": {
                    "min": config["fishing"]["timeouts"]["recast"]["min"],
                    "max": config["fishing"]["timeouts"]["recast"]["max"],
                },
            },
        },
        "colors": {
            "fish-track": (
                config["colors"]["fish-track"]["r"],
                config["colors"]["fish-track"]["g"],
                config["colors"]["fish-track"]["b"],
            )
        },
        "log_lvl": config["log_lvl"],
    }


def save_data(config):
    d = {
        "fishing": {
            "check-area": {
                "x": config["fishing"]["check-area"]["x"].get(),
                "y": config["fishing"]["check-area"]["y"].get(),
                "width": config["fishing"]["check-area"]["width"].get(),
                "height": config["fishing"]["check-area"]["height"].get(),
            },
            "key-binds": {
                "block": config["fishing"]["key-binds"]["block"],
                "cast": config["fishing"]["key-binds"]["cast"],
                "drag-left": config["fishing"]["key-binds"]["drag-left"],
                "drag-right": config["fishing"]["key-binds"]["drag-right"],
            },
            "timeouts": {
                "loop": {
                    "min": config["fishing"]["timeouts"]["loop"]["min"],
                    "max": config["fishing"]["timeouts"]["loop"]["max"],
                },
                "notice-spam": {
                    "min": config["fishing"]["timeouts"]["notice-spam"]["min"],
                    "max": config["fishing"]["timeouts"]["notice-spam"]["max"],
                },
                "reeling": {
                    "min": config["fishing"]["timeouts"]["reeling"]["min"],
                    "max": config["fishing"]["timeouts"]["reeling"]["max"],
                },
                "reeling-pause": {
                    "min": config["fishing"]["timeouts"]["reeling-pause"]["min"],
                    "max": config["fishing"]["timeouts"]["reeling-pause"]["max"],
                },
                "recast": {
                    "min": config["fishing"]["timeouts"]["recast"]["min"],
                    "max": config["fishing"]["timeouts"]["recast"]["max"],
                },
            }
        },
        "colors": {
            "fish-track": {
                "r": config["colors"]["fish-track"][0],
                "g": config["colors"]["fish-track"][1],
                "b": config["colors"]["fish-track"][2],
            },
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