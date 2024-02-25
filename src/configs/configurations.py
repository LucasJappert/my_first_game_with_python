import tkinter
import src.models.utils_models as UtilsModels
from helpers.my_logger_helper import MyLogger

root = tkinter.Tk()

class Configurations:
    grid_size = [100, 100]
    my_screen_size = UtilsModels.Point(root.winfo_screenwidth(), root.winfo_screenheight())

    def __init__(self):
        pass
