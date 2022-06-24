from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(824, 752)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("background-color: rgb(85, 76, 70)")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(140, 100, 581, 491))
        self.frame.setStyleSheet("background-color: rgb(255, 194, 53)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.managerbutton = QtWidgets.QPushButton(self.frame)
        self.managerbutton.setGeometry(QtCore.QRect(150, 270, 291, 41))
        self.managerbutton.setStyleSheet("background-color: rgb(255, 66, 66); font-size: 15pt")
        self.managerbutton.setObjectName("managerbutton")
        self.customerbutton = QtWidgets.QPushButton(self.frame)
        self.customerbutton.setGeometry(QtCore.QRect(150, 210, 291, 41))
        self.customerbutton.setStyleSheet("background-color: rgb(255, 66, 66); font-size: 15pt")
        self.customerbutton.setObjectName("customerbutton")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(250, 170, 101, 31))
        self.label_2.setToolTip("")
        self.label_2.setStatusTip("")
        self.label_2.setWhatsThis("")
        self.label_2.setStyleSheet("font-size: 15pt; background-color: rgb(255, 194, 53)")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(130, 50, 391, 71))
        self.label.setStyleSheet("font-size: 20pt; background-color: rgb(255, 194, 53); color: rgb(0, 0, 0);\n"
"font: 14pt \"Kristen ITC\";")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 824, 26))
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
        self.managerbutton.setText(_translate("MainWindow", "as the Manager"))
        self.customerbutton.setText(_translate("MainWindow", "as a Customer"))
        self.label_2.setText(_translate("MainWindow", "𝑪𝒉𝒐𝒐𝒔𝒆:"))
        self.label.setText(_translate("MainWindow", "𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝒕𝒐 𝒕𝒉𝒆 𝑹𝒆𝒔𝒕𝒂𝒖𝒓𝒂𝒏𝒕"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
