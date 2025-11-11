from yaml import safe_load, dump
from tkinter import IntVar
from utils.global_variables import CONFIG_PATH
from numpy import random

_config = None


def get_config():
    global _config
    if _config is not None:
        return _config
    config = safe_load(open(CONFIG_PATH))

    _config = {
        "fishing": {
            "fish-position": {
                "x": IntVar(value=config["fishing"]["fish-position"]["x"]),
                "y": IntVar(value=config["fishing"]["fish-position"]["y"]),
                "width": IntVar(value=config["fishing"]["fish-position"]["width"]),
                "height": IntVar(value=config["fishing"]["fish-position"]["height"]),
            },
            "fishing-progress": {
                "x": IntVar(value=config["fishing"]["fishing-progress"]["x"]),
                "y": IntVar(value=config["fishing"]["fishing-progress"]["y"]),
                "width": IntVar(value=config["fishing"]["fishing-progress"]["width"]),
                "height": IntVar(value=config["fishing"]["fishing-progress"]["height"]),
            },
            "key-binds": {
                "block": config["fishing"]["key-binds"]["block"],
                "recast": config["fishing"]["key-binds"]["recast"],
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
                "cast": {
                    "min": config["fishing"]["timeouts"]["cast"]["min"],
                    "max": config["fishing"]["timeouts"]["cast"]["max"],
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
    return _config


def save_data():
    d = {
        "fishing": {
            "fish-position": {
                "x": _config["fishing"]["fish-position"]["x"].get(),
                "y": _config["fishing"]["fish-position"]["y"].get(),
                "width": _config["fishing"]["fish-position"]["width"].get(),
                "height": _config["fishing"]["fish-position"]["height"].get(),
            },
            "fishing-progress": {
                "x": _config["fishing"]["fishing-progress"]["x"].get(),
                "y": _config["fishing"]["fishing-progress"]["y"].get(),
                "width": _config["fishing"]["fishing-progress"]["width"].get(),
                "height": _config["fishing"]["fishing-progress"]["height"].get(),
            },
            "key-binds": {
                "block": _config["fishing"]["key-binds"]["block"],
                "recast": _config["fishing"]["key-binds"]["recast"],
                "drag-left": _config["fishing"]["key-binds"]["drag-left"],
                "drag-right": _config["fishing"]["key-binds"]["drag-right"],
            },
            "timeouts": {
                "loop": {
                    "min": _config["fishing"]["timeouts"]["loop"]["min"],
                    "max": _config["fishing"]["timeouts"]["loop"]["max"],
                },
                "notice-spam": {
                    "min": _config["fishing"]["timeouts"]["notice-spam"]["min"],
                    "max": _config["fishing"]["timeouts"]["notice-spam"]["max"],
                },
                "reeling": {
                    "min": _config["fishing"]["timeouts"]["reeling"]["min"],
                    "max": _config["fishing"]["timeouts"]["reeling"]["max"],
                },
                "reeling-pause": {
                    "min": _config["fishing"]["timeouts"]["reeling-pause"]["min"],
                    "max": _config["fishing"]["timeouts"]["reeling-pause"]["max"],
                },
                "recast": {
                    "min": _config["fishing"]["timeouts"]["recast"]["min"],
                    "max": _config["fishing"]["timeouts"]["recast"]["max"],
                },
                "cast": {
                    "min": _config["fishing"]["timeouts"]["cast"]["min"],
                    "max": _config["fishing"]["timeouts"]["cast"]["max"],
                },
            },
        },
        "colors": {
            "fish-track": {
                "r": _config["colors"]["fish-track"][0],
                "g": _config["colors"]["fish-track"][1],
                "b": _config["colors"]["fish-track"][2],
            },
        },
        "log_lvl": _config["log_lvl"],
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
