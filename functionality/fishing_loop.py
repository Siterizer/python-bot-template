from wrappers.logging_wrapper import debug, info
from asyncio import sleep

from functionality.fishing_actions import cast
from functionality.image_recognition import image_recognition_result
from utils.config import get_config


async def fishing_loop():
    # loop = asyncio.get_event_loop()
    config = get_config()
    while True:
        await sleep(1)
        debug("starting new loop")
        await call_appropriate_fishing_action(config)


async def call_appropriate_fishing_action(config):
    recog_result = await image_recognition_result(
        config["fishing"]["fish-position"]["x"].get(),
        config["fishing"]["fish-position"]["y"].get(),
        config["fishing"]["fish-position"]["width"].get(),
        config["fishing"]["fish-position"]["height"].get(),
    )
    info(f"Image recognition result: {recog_result}")
    await cast(config)
