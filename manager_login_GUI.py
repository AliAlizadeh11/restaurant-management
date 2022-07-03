from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, QFrame
import sys


class ManagerLogin(QMainWindow):
    def __init__(self):
        super(ManagerLogin, self).__init__()
        uic.loadUi('manager_login.ui', self)


        self.setWindowTitle("ManagerLogin")
        self.frame = self.findChild(QFrame, 'frame')
        self.label = self.findChild(QLabel, 'label')
        self.username = self.findChild(QLineEdit, 'Username')
        self.password = self.findChild(QLineEdit, 'Password')
        self.button = self.findChild(QPushButton, 'pushButton')
        self.button.clicked.connect(self.managerlog)
        self.Password.setEchoMode(QLineEdit.Password)
        
        

    def managerlog(self):
        if self.username.text == 'koosha' and self.password.text == 'ahmad':
            customerlog = ManagerProfile()
            widget.addWidget(customerlog)
            widget.setCurrentIndex(widget.currentIndex()+1)


    
class ManagerProfile(QMainWindow):
    def __init__(self):
        super(ManagerProfile, self).__init__()
        uic.loadUi('manager_profile.ui', self)



app1 = QApplication(sys.argv)
window1 = ManagerLogin()
widget=QtWidgets.QStackedWidget()
widget.addWidget(window1)
widget.setFixedWidth(1172)
widget.setFixedHeight(823)
widget.show()
app1.exec_()