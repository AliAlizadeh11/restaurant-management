from PyQt5 import QtWidgets, uic , QtGui,QtCore 
from PyQt5.QtWidgets import QMainWindow ,QApplication ,QPushButton, QFrame, QLabel, QLineEdit
import sys


class CustomerSignup(QMainWindow):
    def __init__(self):
        super(CustomerSignup, self).__init__()
        uic.loadUi('customer_signup.ui', self)
        self.button = self.findChild(QPushButton, 'pushButton')
        self.button2 = self.findChild(QPushButton, 'pushButton_2')
        self.button.clicked.connect(self.back_costumerlog)
        self.button2.clicked.connect(self.back_button)

    def back_costumerlog(self):
        back_cl = CustomerLogin()
        widget.addWidget(back_cl)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def back_button(self):
        back_butt = CustomerLogin()
        widget.addWidget(back_butt)
        widget.setCurrentIndex(widget.currentIndex()+1)

class CustomerLogin(QMainWindow):
    def __init__(self):
        super(CustomerLogin, self).__init__()
        uic.loadUi('customer_login.ui', self)


app = QApplication(sys.argv)
window  = CustomerSignup()
widget=QtWidgets.QStackedWidget()
widget.addWidget(window)
widget.setFixedWidth(1261)
widget.setFixedHeight(881)
widget.show()
app.exec_()