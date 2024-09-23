import concurrent.futures
import configparser
import functools
from os import path
from .ImageRecognitionResult import ImageRecognitionResult

import cv2 as cv
from numpy import array
from PIL import ImageGrab
from utils.global_variables import COLOR_WAGES



async def image_recognition_result(ctx, x, y, width, height):
    return ImageRecognitionResult.NOTHING_ON_SCREEN
