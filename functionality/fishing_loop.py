from time import time
from wrappers.logging_wrapper import debug, info
from .PlayerStates import PlayerStates
from .ImageRecognitionResult import ImageRecognitionResult

import asyncio
from functionality.fishing_actions import cast, fish_notice, pause, reel_fish_left, reel_fish_right
from functionality.image_recognition import image_recognition_result


last_player_state = PlayerStates.IDLING
last_image_recog_result = ImageRecognitionResult.NOTHING_ON_SCREEN

async def fishing_loop(config):
    loop = asyncio.get_event_loop()
    ctx = {
        "loop": loop,
        "config": config
    }

    while True:
        debug("starting new loop")
        await call_appropriate_fishing_action(ctx)

async def call_appropriate_fishing_action(ctx):

    result_from_image_recognition = await image_recognition_result(
        ctx,
        ctx["config"]["fishing"]["check-area"]["x"].get(),
        ctx["config"]["fishing"]["check-area"]["y"].get(),
        ctx["config"]["fishing"]["check-area"]["width"].get(),
        ctx["config"]["fishing"]["check-area"]["height"].get(),
    )

    # double checking that it is a correct match
    if (last_image_recog_result != result_from_image_recognition):  
        last_image_recog_result = result_from_image_recognition
        return
    last_image_recog_result = result_from_image_recognition

    # if player in searching state and image result is waiting, then 'spam' notice key trying
    # to start mini-game
    if (last_player_state == PlayerStates.SEARCHING and 
            result_from_image_recognition == ImageRecognitionResult.WAITING_FOR_FISH):
        fish_notice(ctx)
        return
    
    #if player in idling state and image result has found nothing, then cast a fishing rod and
    #change player state to searching
    if (last_player_state == PlayerStates.IDLING and
            result_from_image_recognition == ImageRecognitionResult.NOTHING_ON_SCREEN):
        cast(ctx)
        last_player_state = PlayerStates.SEARCHING
        return
    
    if (result_from_image_recognition == ImageRecognitionResult.READY_TO_REEL_LEFT):
        reel_fish_left(ctx)
        last_player_state = PlayerStates.REELING
        return

    if (result_from_image_recognition == ImageRecognitionResult.READY_TO_REEL_RIGHT):
        reel_fish_right(ctx)
        last_player_state = PlayerStates.REELING
        return
    
    # Last state is reeling and image result found nothing. Probably fish was caught, then
    # change player state to idling.
    if (last_player_state == PlayerStates.REELING and
            result_from_image_recognition == ImageRecognitionResult.NOTHING_ON_SCREEN):
        last_player_state = PlayerStates.IDLING
        return
    
    if (result_from_image_recognition == ImageRecognitionResult.STOP_THE_REEL):
        last_player_state = PlayerStates.WAITING
        pause(ctx)
        return
    
    #finally blocks. If code enters here something wrong happened.
    if (result_from_image_recognition == ImageRecognitionResult.NOTHING_ON_SCREEN):
        last_player_state = PlayerStates.IDLING
        return
    if (result_from_image_recognition == ImageRecognitionResult.WAITING_FOR_FISH):
        last_player_state = PlayerStates.SEARCHING
        return
    