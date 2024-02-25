import tkinter
import models.utils_models as UtilsModels
from helpers.my_logger import MyLogger

root = tkinter.Tk()

class Configurations:
    grid_size = [100, 100]
    my_screen_size = UtilsModels.Point(root.winfo_screenwidth(), root.winfo_screenheight())

    def __init__(self):
        pass
