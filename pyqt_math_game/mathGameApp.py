from PyQt5.QtWidgets import QApplication

from pyqt_style_setter import StyleSetter
from pyqt_custom_titlebar_setter import CustomTitlebarSetter

from pyqt_math_game import MathGame


class MathGameApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        mainWindow = MathGame()
        StyleSetter.setWindowStyle(mainWindow)
        self.__titleBarWindow = CustomTitlebarSetter.getCustomTitleBar(mainWindow, icon_filename='ico/math.svg')
        self.__titleBarWindow.show()