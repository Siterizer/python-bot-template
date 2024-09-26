from utils.config import random_timeout

from asyncio import sleep
from wrappers.win32api_wrapper import (
    release_key,
    press_key,
)
from wrappers.logging_wrapper import debug


async def fish_notice(ctx):
    notice_timeout = await random_timeout(ctx["config"]["fishing"]["timeouts"]["notice"])
    notice_key = ctx["config"]["fishing"]["key-binds"]["block"]
    debug(f"Press {notice_key} keyboard key for: {notice_timeout} s in order to init fishing game")
    await press_key(ctx, notice_key)
    await sleep(notice_timeout)
    await release_key(ctx, notice_key)

async def reel_fish_right(ctx):
    reel_timeout = await random_timeout(ctx["config"]["fishing"]["timeouts"]["reeling"])
    reel_key = ctx["config"]["fishing"]["key-binds"]["drag-right"]
    debug(f"Press {reel_key} keyboard key for: {reel_timeout} s in order to reel right a fish")
    await press_key(ctx, reel_key)
    await sleep(reel_timeout)
    await release_key(ctx, reel_key)

async def reel_fish_left(ctx):
    reel_timeout = await random_timeout(ctx["config"]["fishing"]["timeouts"]["reeling"])
    reel_key = ctx["config"]["fishing"]["key-binds"]["drag-left"]
    debug(f"Press {reel_key} keyboard key for: {reel_timeout} s in order to reel left a fish")
    await press_key(ctx, reel_key)
    await sleep(reel_timeout)
    await release_key(ctx, reel_key)

async def pause(ctx):
    reel_pause = await random_timeout(ctx["config"]["fishing"]["timeouts"]["reeling-pause"])
    debug(f"Stamina at critical level. Waiting for: {reel_pause} s")
    await sleep(reel_pause)

async def cast(ctx):
    recast_timeout = await random_timeout(ctx["config"]["fishing"]["timeouts"]["recast"])
    debug(f"Recasting rod. Waiting for: {recast_timeout} s")
    await sleep(recast_timeout)
    cast_key = ctx["config"]["fishing"]["key-binds"]["recast"]
    cast_timeout = await random_timeout(ctx["config"]["fishing"]["timeouts"]["cast"])
    debug(f"Press {cast_key} keyboard key for: {cast_timeout} s in order to recast a rod")
    await press_key(ctx, cast_key)
    await sleep(cast_timeout)
    await release_key(ctx, cast_key)
