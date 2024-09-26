from enum import Enum

class ImageRecognitionResult:
    NOTHING_ON_SCREEN = 0
    WAITING_FOR_FISH = 1
    READY_TO_REEL_LEFT = 2
    READY_TO_REEL_RIGHT = 3
    STOP_THE_REEL = 4