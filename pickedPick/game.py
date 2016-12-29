#! /usr/bin/env python
# encoding=utf-8
"""
@version:??
@author:都真全
@time:2016/12/24 9:35
"""
import sys
from PyQt5.QtWidgets import (QLabel,QLineEdit,QPushButton,QWidget,
                             QGridLayout,QApplication,QMessageBox,QMainWindow,QComboBox)
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication
import random as rd

temp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alpha = temp
class UI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        widget = QWidget(self)
        grid = QGridLayout(widget)

        palette = QtGui.QPalette()
        palette.setColor(self.backgroundRole(),QColor(192,253,123))
        self.setCentralWidget(widget)
        self.teachersNumlabel = QLabel("    老师人数:",self)
        self.studentNumLabel = QLabel("      学生人数:",self)

        self.teachersNumlineEdit = QLineEdit("15")
        self.studentNumlineEdit = QLineEdit("119")
        self.combo = QComboBox(self)
        self.combo.addItem("抽取老师")
        self.combo.addItem("抽取学生")
        self.combo.addItem("抽取全部")
        self.combo.activated[str].connect(self.onActivated)

        self.button1 = QPushButton("第一组")
        self.button1.clicked.connect(self.randoms)
        self.LineEdit10 = QLineEdit()
        self.LineEdit11 = QLineEdit()
        self.LineEdit12 = QLineEdit()
        self.LineEdit13 = QLineEdit()
        self.LineEdit14 = QLineEdit()

        self.button2 = QPushButton("第二组")
        self.button2.clicked.connect(self.randoms)
        self.LineEdit20 = QLineEdit()
        self.LineEdit21 = QLineEdit()
        self.LineEdit22 = QLineEdit()
        self.LineEdit23 = QLineEdit()
        self.LineEdit24 = QLineEdit()

        self.button3 = QPushButton("第三组")
        self.button3.clicked.connect(self.randoms)
        self.LineEdit30 = QLineEdit()
        self.LineEdit31 = QLineEdit()
        self.LineEdit32 = QLineEdit()
        self.LineEdit33 = QLineEdit()
        self.LineEdit34 = QLineEdit()

        self.button4 = QPushButton("第四组")
        self.button4.clicked.connect(self.randoms)
        self.LineEdit40 = QLineEdit()
        self.LineEdit41 = QLineEdit()
        self.LineEdit42 = QLineEdit()
        self.LineEdit43 = QLineEdit()
        self.LineEdit44 = QLineEdit()

        self.button5 = QPushButton("第五组")
        self.button5.clicked.connect(self.randoms)
        self.LineEdit50 = QLineEdit()
        self.LineEdit51 = QLineEdit()
        self.LineEdit52 = QLineEdit()
        self.LineEdit53 = QLineEdit()
        self.LineEdit54 = QLineEdit()

        self.clearButton = QPushButton("清空")
        self.clearButton.clicked.connect(self.clear)


        position = [(i,j) for i in range(6) for j in range(6)]

        # print(position[6:12])
        # print(position[12:18])

        grid.addWidget(self.teachersNumlabel,*position[0])
        grid.addWidget(self.teachersNumlineEdit,*position[1])
        grid.addWidget(self.studentNumLabel,*position[2])
        grid.addWidget(self.studentNumlineEdit,*position[3])
        grid.addWidget(self.combo,*position[4])
        grid.addWidget(self.clearButton,*position[5])

        grid.addWidget(self.button1,*position[6])
        grid.addWidget(self.LineEdit10,*position[7])
        grid.addWidget(self.LineEdit11, *position[8])
        grid.addWidget(self.LineEdit12, *position[9])
        grid.addWidget(self.LineEdit13, *position[10])
        grid.addWidget(self.LineEdit14, *position[11])

        grid.addWidget(self.button2, *position[12])
        grid.addWidget(self.LineEdit20, *position[13])
        grid.addWidget(self.LineEdit21, *position[14])
        grid.addWidget(self.LineEdit22, *position[15])
        grid.addWidget(self.LineEdit23, *position[16])
        grid.addWidget(self.LineEdit24, *position[17])

        grid.addWidget(self.button3, *position[18])
        grid.addWidget(self.LineEdit30, *position[19])
        grid.addWidget(self.LineEdit31, *position[20])
        grid.addWidget(self.LineEdit32, *position[21])
        grid.addWidget(self.LineEdit33, *position[22])
        grid.addWidget(self.LineEdit34, *position[23])

        grid.addWidget(self.button4, *position[24])
        grid.addWidget(self.LineEdit40, *position[25])
        grid.addWidget(self.LineEdit41, *position[26])
        grid.addWidget(self.LineEdit42, *position[27])
        grid.addWidget(self.LineEdit43, *position[28])
        grid.addWidget(self.LineEdit44, *position[29])

        grid.addWidget(self.button5, *position[30])
        grid.addWidget(self.LineEdit50, *position[31])
        grid.addWidget(self.LineEdit51, *position[32])
        grid.addWidget(self.LineEdit52, *position[33])
        grid.addWidget(self.LineEdit53, *position[34])
        grid.addWidget(self.LineEdit54, *position[35])

        self.setPalette(palette)
        self.setAutoFillBackground(True)
        self.setGeometry(300,300,600,300)
        self.setWindowTitle('pickedPick')
        self.show()
    def randoms(self):
        sender = self.sender()
        flag = self.combo.currentText()
        if flag == "抽取老师":
            teacherId = self.randomTeachers(sender)
            self.group2lineEdit(sender,teacherId)
        elif flag == "抽取学生":
            studentId =self.randomStudents(sender)
            self.group2lineEdit(sender, studentId)
        else:
            allId = self.randomAll(sender)
            self.group2lineEdit(sender, allId)

    def randomTeachers(self,sender):
        # print(sender.text())
        teacherNum =self.teachersNumlineEdit.text()
        temp = int(teacherNum)
        teacherId = alpha[rd.randint(0,temp)]
        alpha.remove(teacherId)
        return teacherId
    def randomStudents(self,sender):
        # print(sender.text())
        studentNum = self.studentNumlineEdit.text()
        temp = int(studentNum)
        studentId = str(rd.randint(1,temp))
        return studentId
    def randomAll(self,sender):
        # print(sender.text())
        all = []
        teacherNum = self.teachersNumlineEdit.text()
        temp1 = int(teacherNum)
        studentNum = self.studentNumlineEdit.text()
        temp2 = int(studentNum)
        all.extend(alpha[0:1+temp1])
        all.extend(range(1,temp2))
        allId = str(all[rd.randint(1,temp1+temp2)])
        return allId

    def onActivated(self,text):
        self.actived= text

    def group2lineEdit(self,sender,Id):
        if sender.text()=="第一组":
            if self.LineEdit10.text() == "":
                 self.LineEdit10.setText(Id)
            elif self.LineEdit11.text() == "":
                 self.LineEdit11.setText(Id)
            elif self.LineEdit12.text() == "":
                 self.LineEdit12.setText(Id)
            elif self.LineEdit13.text() =="":
                self.LineEdit13.setText(Id)
            else:
                self.LineEdit14.setText(Id)
        elif sender.text()=="第二组":
            if self.LineEdit20.text() == "":
                 self.LineEdit20.setText(Id)
            elif self.LineEdit21.text() == "":
                 self.LineEdit21.setText(Id)
            elif self.LineEdit22.text() == "":
                 self.LineEdit22.setText(Id)
            elif self.LineEdit23.text() =="":
                self.LineEdit23.setText(Id)
            else:
                self.LineEdit24.setText(Id)
        elif sender.text()=="第三组":
            if self.LineEdit30.text() == "":
                 self.LineEdit30.setText(Id)
            elif self.LineEdit31.text() == "":
                 self.LineEdit31.setText(Id)
            elif self.LineEdit32.text() == "":
                 self.LineEdit32.setText(Id)
            elif self.LineEdit33.text() =="":
                self.LineEdit33.setText(Id)
            else:
                self.LineEdit34.setText(Id)
        elif sender.text()=="第四组":
            if self.LineEdit40.text() == "":
                 self.LineEdit40.setText(Id)
            elif self.LineEdit41.text() == "":
                 self.LineEdit41.setText(Id)
            elif self.LineEdit42.text() == "":
                 self.LineEdit42.setText(Id)
            elif self.LineEdit43.text() =="":
                self.LineEdit43.setText(Id)
            else:
                self.LineEdit44.setText(Id)
        else:
            if self.LineEdit50.text() == "":
                 self.LineEdit50.setText(Id)
            elif self.LineEdit51.text() == "":
                 self.LineEdit51.setText(Id)
            elif self.LineEdit52.text() == "":
                 self.LineEdit52.setText(Id)
            elif self.LineEdit53.text() =="":
                self.LineEdit53.setText(Id)
            else:
                self.LineEdit54.setText(Id)
    def clear(self):
        alpha = temp
        self.LineEdit10.clear()
        self.LineEdit11.clear()
        self.LineEdit12.clear()
        self.LineEdit13.clear()
        self.LineEdit14.clear()
        self.LineEdit20.clear()
        self.LineEdit21.clear()
        self.LineEdit22.clear()
        self.LineEdit23.clear()
        self.LineEdit24.clear()
        self.LineEdit30.clear()
        self.LineEdit31.clear()
        self.LineEdit32.clear()
        self.LineEdit33.clear()
        self.LineEdit34.clear()
        self.LineEdit40.clear()
        self.LineEdit41.clear()
        self.LineEdit42.clear()
        self.LineEdit43.clear()
        self.LineEdit44.clear()
        self.LineEdit50.clear()
        self.LineEdit51.clear()
        self.LineEdit52.clear()
        self.LineEdit53.clear()
        self.LineEdit54.clear()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = UI()
    sys.exit(app.exec_())