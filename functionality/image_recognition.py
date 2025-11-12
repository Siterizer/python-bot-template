from wrappers.logging_wrapper import debug
from .ImageRecognitionResult import ImageRecognitionResult


async def image_recognition_result(x, y, width, height):
    debug(f"image_recognition_result based on  x: {x}, y: {y}, width: {width}, height: {height} ")
    return ImageRecognitionResult.NOTHING_ON_SCREEN
