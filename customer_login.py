from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(835, 765)
        MainWindow.setStyleSheet("background-color: rgb(85, 76, 70)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(160, 70, 541, 571))
        self.frame.setStyleSheet("background-color: rgb(255, 194, 53)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(90, 20, 381, 71))
        self.label.setStyleSheet("font-size: 30pt")
        self.label.setObjectName("label")
        self.Username = QtWidgets.QLineEdit(self.frame)
        self.Username.setGeometry(QtCore.QRect(140, 110, 251, 41))
        self.Username.setStyleSheet("background-color: rgb(255, 255, 255); font-size: 10pt")
        self.Username.setObjectName("Username")
        self.Password = QtWidgets.QLineEdit(self.frame)
        self.Password.setGeometry(QtCore.QRect(140, 170, 251, 41))
        self.Password.setStyleSheet("background-color: rgb(255, 255, 255); font-size: 10pt")
        self.Password.setDragEnabled(False)
        self.Password.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.Password.setObjectName("Password")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(140, 260, 251, 41))
        self.pushButton.setStyleSheet("background-color: rgb(255, 66, 66); font-size: 15pt")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(140, 320, 161, 31))
        self.label_3.setStyleSheet("font-size: 9pt")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 320, 91, 28))
        self.pushButton_2.setStyleSheet("background-color:  rgb(255, 66, 66);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font-size: 8pt")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 370, 111, 28))
        self.pushButton_3.setStyleSheet("background-color:  rgb(255, 66, 66);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font-size: 8pt")
        self.pushButton_3.setObjectName("pushButton_3")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(140, 220, 111, 20))
        self.checkBox.setObjectName("checkBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 835, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "𝑨𝑷 𝑹𝒆𝒔𝒕𝒂𝒖𝒓𝒂𝒏𝒕"))
        self.Username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.Password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.label_3.setText(_translate("MainWindow", "Don\'t have an account?"))
        self.pushButton_2.setText(_translate("MainWindow", "Sign up"))
        self.pushButton_3.setText(_translate("MainWindow", "Forget password?"))
        self.checkBox.setText(_translate("MainWindow", "Remember me"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())