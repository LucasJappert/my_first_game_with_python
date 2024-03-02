import random
from src.models.utils_models import Point
from src.utils.camera_variables import CAMERA_VARIABLES

def get_randome_tile():
    result: Point = Point(0, 0)
    result.x = random.randint(0, CAMERA_VARIABLES.tiles.x -1)
    result.y = random.randint(0, CAMERA_VARIABLES.tiles.y -1)
    return result
