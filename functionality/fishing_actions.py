from utils.config import random_timeout

from asyncio import sleep
from wrappers.logging_wrapper import debug
from wrappers.win32api_wrapper import press_key, release_key, click_mouse_with_coordinates


async def cast(event_loop, config):
    recast_timeout = await random_timeout(config["fishing"]["timeouts"]["recast"])
    debug(f"Recasting rod. Waiting for: {recast_timeout} s")
    await sleep(recast_timeout)

    debug(f"Moving mouse to cooridates x: {config['fishing']['fish-position']['x'].get()}, y: {config['fishing']['fish-position']['y'].get()}")
    await click_mouse_with_coordinates(event_loop, config["fishing"]["fish-position"]["x"].get(), config["fishing"]["fish-position"]["y"].get())
    await sleep(recast_timeout)

    debug(f"Clicking: {config['fishing']['key-binds']['recast']} keyboard key")
    await press_key(event_loop, config["fishing"]["key-binds"]["recast"])
    await sleep(0.1)
    await release_key(event_loop, config["fishing"]["key-binds"]["recast"])
