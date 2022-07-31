import sys
from PyQt5.QtWidgets import *
from calcmodel import CalcModel
from calcview import CalcView
from calccontroller import CalcController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #
    model = CalcModel()
    view = CalcView()
    controller = CalcController(model, view)
    view.show()
    #
    app.exec_()
