from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import requests
import sys

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.frameGeometry().center()
        self.setFixedSize(300,150)
        self.setContentsMargins(10,10,10,10)
        self.setWindowTitle("Mini Lotto Combinator")
        self.icon = QIcon("lottery.svg")
        self.setWindowIcon(self.icon)
        self.createLayout()
        self.show()

    def createLayout(self):
        self.gBox = QGroupBox()
        layout = QGridLayout()
        layout.setColumnStretch(1,5)
        layout.setColumnStretch(2,5)

        self.okBtn = QPushButton("Ok")
        self.okBtn2 = QPushButton("Ok")
        self.okBtn3 = QPushButton("Ok")
        self.okBtn4 = QPushButton("Ok")
        self.okBtn5 = QPushButton("Ok")
        self.okBtn6 = QPushButton("Ok")
        self.okBtn7 = QPushButton("Ok")

        self.okBtn.clicked.connect(pyqtSlot(name="ok"))

        layout.addWidget(self.okBtn,1,1)
        layout.addWidget(self.okBtn2,1,2)
        layout.addWidget(self.okBtn3,1,3)
        layout.addWidget(self.okBtn4,1,4)
        layout.addWidget(self.okBtn5,2,1,1,2)
        layout.addWidget(self.okBtn6,2,3,1,2)
        layout.addWidget(self.okBtn7,3,1,1,4)

        self.setLayout(layout)

    @pyqtSlot(name="ok",result="QFrame")
    def ok(self):
        return print('ok')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

