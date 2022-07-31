import os.path
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)
myworkdir = dname.replace("\\","/")

CalcWindow = uic.loadUiType(f"{myworkdir}/calcview.ui")[0]


class CalcView(CalcWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    # def btn_equal_slot(self, f):
    #     self.btn_equal.clicked.connect(self.f)

    def getNum1(self):
        return self.txt_num1.text()
    def getNum2(self):
        return self.txt_num2.text()

    def setResult(self, sn):
        self.txt_result.setText(sn)

