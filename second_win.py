# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QLineEdit
from instr import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
    def initUI(self):
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()
        self.text_name = QLabel(txt_name)
        self.text_age = QLabel(txt_age)
        self.line_name = QLineEdit(txt_hintname)
        self.line_age = QLineEdit(txt_hintage)
        self.text_test1 = QLabel(txt_test1)
        self.text_test2 = QLabel(txt_test2)
        self.text_test3 = QLabel(txt_test3)
        self.line_test1 = QLineEdit(txt_hinttest1)
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test3 = QLineEdit(txt_hinttest3)
        self.button_test1 = QPushButton(txt_starttest1, parent=self)
        self.button_test2 = QPushButton(txt_starttest2, parent=self)
        self.button_test3 = QPushButton(txt_starttest3, parent=self)
        self.button_next = QPushButton(txt_sendresults, parent=self)
        self.l_line.addWidget(self.text_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test1, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.button_test1, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.text_test2, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.button_test2, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.text_test3, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.button_test3, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.button_next, alignment= Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    def next_click(self):
        self.hide()
        self.fw = FinalWin()
    def connects(self):
        self.button_next.clicked.connect(self.next_click)
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)  