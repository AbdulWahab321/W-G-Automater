# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Python_Projects\PyQt5 Progress Bar\tth.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from actions import Main

color = [0,0,255]

def change_color(main_widget):
    global color
    clr = Main.get_rgb(main_widget)
    
    red = clr[0]
    green = clr[1]
    blue = clr[2]    
    
    color = [red,green,blue]

def create_image(main_widget,text_input):
    import socket
    if socket.gethostbyname(socket.gethostname())!="127.0.0.1":
        clr = color
        
        red = clr[0]
        green = clr[1]
        blue = clr[2]
                
        Main.Text_To_Handwrite.create_hnd_wrt(Main.Text_To_Handwrite,main_widget,text_input.toPlainText(),red,green,blue)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(835, 580)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(90, -10, 671, 101))
        self.title.setObjectName("title")
        self.your_text_label = QtWidgets.QLabel(self.centralwidget)
        self.your_text_label.setGeometry(QtCore.QRect(10, 110, 101, 41))
        self.your_text_label.setObjectName("your_text_label")
        self.text_hndwrt_input = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_hndwrt_input.setGeometry(QtCore.QRect(110, 120, 601, 241))
        self.text_hndwrt_input.setObjectName("text_hndwrt_input")
        self.save_btn = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:create_image(self.centralwidget,self.text_hndwrt_input))
        self.save_btn.setGeometry(QtCore.QRect(250, 450, 321, 41))
        self.save_btn.setObjectName("save_btn")
        self.color_change_btn = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:change_color(self.centralwidget))
        self.color_change_btn.setGeometry(QtCore.QRect(330, 380, 171, 41))
        self.color_change_btn.setObjectName("color_change_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Text to Handwriter"))
        self.title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">Text To Handwriting</span></p></body></html>"))
        self.your_text_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Your Text:</span></p></body></html>"))
        self.save_btn.setText(_translate("MainWindow", "Create An Image From Text (Handwriting)"))
        self.color_change_btn.setText(_translate("MainWindow", "Change Handwriting Color"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
