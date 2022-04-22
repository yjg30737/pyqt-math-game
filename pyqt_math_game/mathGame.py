from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QPushButton, QMainWindow

from pymeg import ExpStruct, ExpGenerator
from pyqt_responsive_label import ResponsiveLabel
from pyqt_rounded_corners_lineedit import RoundedCornersLineEdit
from pyqt_style_setter import StyleSetter
from pyqt_toast import Toast


class MathGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setWindowTitle('Math Game')

        self.__initProblem()
        self.__mathProblemLbl = ResponsiveLabel(self)
        self.__mathProblemLbl.setAcceptTextChange(True)
        self.__setProblem()

        btn = QPushButton('Try other')
        btn.clicked.connect(self.__setProblem)
        self.__submitLineEdit = RoundedCornersLineEdit()
        self.__submitLineEdit.returnPressed.connect(self.__submitAnswer)
        self.__submitBtn = QPushButton('Submit')
        self.__submitBtn.clicked.connect(self.__submitAnswer)

        lay = QGridLayout()
        lay.addWidget(self.__mathProblemLbl, 0, 0, 1, 1)
        lay.addWidget(self.__submitLineEdit, 1, 0, 1, 1)
        lay.addWidget(self.__submitBtn, 1, 1, 1, 1)
        lay.addWidget(btn, 0, 1, 1, 1)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)

        self.setMinimumSize(self.sizeHint())

        self.setCentralWidget(mainWidget)

    def __initProblem(self):
        self.__problem = ExpStruct()
        self.__problem.set_op([ExpStruct.PLUS, ExpStruct.MINUS])
        self.__problem.set_oper_cnt(3)

    def __setProblem(self):
        ext = self.__getProblem()
        self.__mathProblemLbl.setText(ext)

    def __submitAnswer(self):
        answer = str(eval(self.__mathProblemLbl.text()))
        if self.__submitLineEdit.text() == answer:
            toast = Toast(text='Right', duration=2, parent=self)
            toast.show()
        else:
            toast = Toast(text='Wrong', duration=2, parent=self)
            toast.show()
        self.__submitLineEdit.clear()
        self.__setProblem()

    def __getProblem(self):
        ext = ExpGenerator.get_problem(self.__problem)
        return ext


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mathGame = MathGame()
    StyleSetter.setWindowStyle(mathGame)
    mathGame.show()
    app.exec_()
