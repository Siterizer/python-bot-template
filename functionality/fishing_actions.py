from utils.config import random_timeout

from asyncio import sleep
from wrappers.logging_wrapper import debug


async def cast(config):
    recast_timeout = await random_timeout(config["fishing"]["timeouts"]["recast"])
    debug(f"Recasting rod. Waiting for: {recast_timeout} s")
    await sleep(recast_timeout)
