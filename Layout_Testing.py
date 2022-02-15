import sys

from PyQt5.QtWidgets import (QApplication,QHBoxLayout, QVBoxLayout, QPushButton, QWidget, QGridLayout)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.resize(500, 500)
        layout = QGridLayout()
        self.b1 = QPushButton("7")
        self.b1.clicked.connect(self.btnstate)
        layout.addWidget(self.b1, 0, 0)
        self.b2 = QPushButton("8")
        self.b2.clicked.connect(self.btnstate)
        layout.addWidget(self.b2, 0, 1)
        self.b3 = QPushButton("9")
        self.b3.clicked.connect(self.btnstate)
        layout.addWidget(self.b3, 0, 2)
        self.b4 = QPushButton("+")
        self.b4.clicked.connect(self.btnstate)
        layout.addWidget(self.b4, 0, 3)
        self.b5 = QPushButton("4")
        self.b5.clicked.connect(self.btnstate)
        layout.addWidget(self.b5, 1, 0)
        self.b6 = QPushButton("5")
        self.b6.clicked.connect(self.btnstate)
        layout.addWidget(self.b6, 1, 1)
        self.b7 = QPushButton("6")
        self.b7.clicked.connect(self.btnstate)
        layout.addWidget(self.b7, 1, 2)
        self.b8 = QPushButton("-")
        self.b8.clicked.connect(self.btnstate)
        layout.addWidget(self.b8, 1, 3)
        self.b9 = QPushButton("1")
        self.b9.clicked.connect(self.btnstate)
        layout.addWidget(self.b9, 2, 0)
        self.b10 = QPushButton("2")
        self.b10.clicked.connect(self.btnstate)
        layout.addWidget(self.b10, 2, 1)
        self.b11 = QPushButton("3")
        self.b11.clicked.connect(self.btnstate)
        layout.addWidget(self.b11, 2, 2)
        self.b12 = QPushButton("*")
        self.b12.clicked.connect(self.btnstate)
        layout.addWidget(self.b12, 2, 3)
        self.b13 = QPushButton(".")
        self.b13.clicked.connect(self.btnstate)
        layout.addWidget(self.b13, 3, 0)
        self.b14 = QPushButton("0")
        self.b14.clicked.connect(self.btnstate)
        layout.addWidget(self.b14, 3, 1)
        self.b15 = QPushButton("=")
        self.b15.clicked.connect(self.btnstate)
        layout.addWidget(self.b15, 3, 2)
        self.b16 = QPushButton("/")
        self.b16.clicked.connect(self.btnstate)
        layout.addWidget(self.b16, 3, 3)
        self.setLayout(layout)
        print(self.children())

    def btnstate(self):
        if self.b1.isEnabled():
            print("7")
        if self.b2.isEnabled():
            print("8")
        if self.b3.isEnabled():
            print("9")
        if self.b4.isEnabled():
            print("+")
        if self.b5.isEnabled():
            print("4")
        if self.b6.isEnabled():
            print("5")
        if self.b7.isEnabled():
            print("6")
        if self.b8.isEnabled():
            print("-")
        if self.b9.isEnabled():
            print("1")
        if self.b10.isEnabled():
            print("2")
        if self.b11.isEnabled():
            print("3")
        if self.b12.isEnabled():
            print("*")
        if self.b13.isEnabled():
            print(".")
        if self.b14.isEnabled():
            print("0")
        if self.b15.isEnabled():
            print("=")
        if self.b16.isEnabled():
            print("/")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())