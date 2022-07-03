from PyQt5 import QtWidgets, uic , QtGui,QtCore 
from PyQt5.QtWidgets import QMainWindow ,QApplication ,QPushButton, QFrame, QLabel, QLineEdit
import sys


class CustomerLogin(QMainWindow):
    def __init__(self):
        super(CustomerLogin, self).__init__()
        uic.loadUi('customer_login.ui', self)
        self.button1 = self.findChild(QPushButton, 'CustomerLogin')
        self.button2 = self.findChild(QPushButton, 'CustomerSignup')
        self.button3 = self.findChild(QPushButton, 'ForgerPass')
        self.button1.clicked.connect(self.customerlog)
        self.button2.clicked.connect(self.customersu)
        self.button3.clicked.connect(self.forgetpassword)

    def customerlog(self):
        customerpro = CustomerProfile()
        widget.addWidget(customerpro)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def customersu(self):
        customersign = CustomerSignup()
        widget.addWidget(customersign)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def forgetpassword(self):
        pass


class CustomerProfile(QMainWindow):
    def __init__(self):
        super(CustomerProfile, self).__init__()
        uic.loadUi('menu_and_customerprofile.ui', self)

class CustomerSignup(QMainWindow):
    def __init__(self):
        super(CustomerSignup, self).__init__()
        uic.loadUi('customer_signup.ui', self)

app = QApplication(sys.argv)
window2  = CustomerLogin()
widget=QtWidgets.QStackedWidget()
widget.addWidget(window2)
widget.setFixedWidth(1127)
widget.setFixedHeight(823)
widget.show()
app.exec_()