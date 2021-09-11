from PyQt5 import QtCore, QtWidgets
from msgboxpy import *
from cmpt.pywhatkit.exceptions import InternetException
try:
    from actions import *        
    import actions as acts 
    
    import cmpt.pywhatkit as pywhatkit
except InternetException:
    alert("No internet connection available",Styles.Icons.ICON_ERROR,"ERROR")    
def back(mw):
    mw.destroy()
    os.system('"whatsapp automater.exe"')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 530)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 781, 101))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked =lambda:Main.open_mw(MainWindow))
        self.pushButton.setGeometry(QtCore.QRect(40, 130, 231, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget,clicked =lambda:Main.open_mgw())
        self.pushButton_2.setGeometry(QtCore.QRect(470, 130, 231, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(230, 190, 311, 141))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox,clicked = lambda:Main.History.show_history())
        self.pushButton_3.setGeometry(QtCore.QRect(20, 30, 121, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox,clicked = lambda:Main.History.history_exporter())
        self.pushButton_4.setGeometry(QtCore.QRect(170, 30, 121, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox,clicked = lambda:Main.bug_reporter())
        self.pushButton_5.setGeometry(QtCore.QRect(20, 70, 121, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox,clicked = lambda:Main.History.clear_history())
        self.pushButton_6.setGeometry(QtCore.QRect(170, 70, 121, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        
        self.back = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:back(MainWindow))
        self.back.setGeometry(QtCore.QRect(290, 380, 191, 41))
        self.back.setObjectName("pushButton_6")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Auto Whatsapp Messager Menu"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Auto Whatsapp Messager Menu</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Auto Whatsapp Contact Messager"))
        self.pushButton_2.setText(_translate("MainWindow", "Auto Whatsapp Group Messager"))
        self.groupBox.setTitle(_translate("MainWindow", "                                           Others"))
        self.pushButton_3.setText(_translate("MainWindow", "Show History"))
        self.pushButton_4.setText(_translate("MainWindow", "Export History"))
        self.pushButton_5.setText(_translate("MainWindow", "Report a Bug"))
        self.pushButton_6.setText(_translate("MainWindow", "Clear History"))

        self.back.setText(_translate("MainWindow", "Back"))    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    acts.window = MainWindow
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
