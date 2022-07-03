from PyQt5 import QtWidgets, uic , QtGui,QtCore 
from PyQt5.QtWidgets import QMainWindow ,QApplication ,QPushButton, QFrame, QLabel, QLineEdit, QTableWidget, QAbstractButton, QListWidget, QCalendarWidget, QMessageBox
import sys

class ManagerProfile(QMainWindow):
    def __init__(self):
        super(ManagerProfile, self).__init__()
        uic.loadUi('manager_profile.ui', self)
        self.lineedit1 = self.findChild(QLineEdit, 'lineEdit')
        self.lineedit2 = self.findChild(QLineEdit, 'lineEdit_2')
        self.lineedit3 = self.findChild(QLineEdit, 'lineEdit_3')
        self.lineedit4 = self.findChild(QLineEdit, 'lineEdit_5')
        self.lineedit5 = self.findChild(QLineEdit, 'lineEdit_4')
        self.lineedit6 = self.findChild(QLineEdit, 'lineEdit_22')
        self.label1 = self.findChild(QLabel, 'label_63')
        self.label2 = self.findChild(QLabel, 'label_66')
        self.label3 = self.findChild(QLabel, 'label_65')
        self.label4 = self.findChild(QLabel, 'label_64')
        self.label5 = self.findChild(QLabel, 'label_67')
        self.label6 = self.findChild(QLabel, 'label_68')
        self.button = self.findChild(QPushButton, 'pushButton_7')
        self.add_button = self.findChild(QPushButton, 'pushButton_4')
        self.send_discount = self.findChild(QPushButton, 'pushButton_2')
        self.edit_menu = self.findChild(QPushButton, 'pushButton_5')
        self.confrim_order = self.findChild(QPushButton, 'pushButton_6')
        self.button.clicked.connect(self.edit)
        self.add_button.clicked.connect(self.add)
        self.send_discount.clicked.connect(self.send)
        self.edit_menu.clicked.connect(self.editing_menu)
        self.confrim_order.clicked.connect(self.confirming)
        self.lineedit7 = self.findChild(QLineEdit, 'lineEdit_6')
        self.lineedit8 = self.findChild(QLineEdit, 'lineEdit_7')
        self.lineedit9 = self.findChild(QLineEdit, 'lineEdit_8')
        self.lineedit10 = self.findChild(QLineEdit, 'lineEdit_9')
        self.lineedit11 = self.findChild(QLineEdit, 'lineEdit_10')
        self.lineedit12 = self.findChild(QLineEdit, 'lineEdit_11')
        self.lineedit13 = self.findChild(QLineEdit, 'lineEdit_12')
        self.lineedit14 = self.findChild(QLineEdit, 'lineEdit_18')
        self.lineedit15 = self.findChild(QLineEdit, 'lineEdit_13')
        self.lineedit16 = self.findChild(QLineEdit, 'lineEdit_14')
        self.lineedit17 = self.findChild(QLineEdit, 'lineEdit_15')
        self.lineedit18 = self.findChild(QLineEdit, 'lineEdit_19')
        self.lineedit19 = self.findChild(QLineEdit, 'lineEdit_16')
        self.lineedit20 = self.findChild(QLineEdit, 'lineEdit_17')
        self.lineedit21 = self.findChild(QLineEdit, 'lineEdit_20')
        self.lineedit22 = self.findChild(QLineEdit, 'lineEdit_21')

        self.lineedit23 = self.findChild(QLineEdit, 'lineEdit_53')
        self.lineedit24 = self.findChild(QLineEdit, 'lineEdit_54')
        self.lineedit25 = self.findChild(QLineEdit, 'lineEdit_55')
        self.lineedit26 = self.findChild(QLineEdit, 'lineEdit_56')
        self.lineedit27 = self.findChild(QLineEdit, 'lineEdit_57')
        self.lineedi28 = self.findChild(QLineEdit, 'lineEdit_58')
        self.lineedit29 = self.findChild(QLineEdit, 'lineEdit_59')
        self.lineedit30 = self.findChild(QLineEdit, 'lineEdit_60')
        self.list1 = self.findChild(QListWidget, 'listWidget_6')

    def editing_menu(self):
        menu_list = ['Spicy Lobster', 'Baked Scargot', 'Shrimp Cocktail', 'SeaRed Ahi Tuna', 'Filet Mignon, 8ounce', 'Filet Mignon, 12ounce', 'Rib Eye Steak, 18ounce', 'Porter house for two', 'Spinach Salad', 'Caprese Salad', 'French Onion Salad', 'Lobster Bisque', 'Tea', 'Coffe', 'Coca', 'Orange Juice']
        if self.lineedit27.text() in menu_list:
            print(True)
    
    
    def confirming(self):
        pass


    def add(self):
        self.list1.addItem(f'{self.lineedit23.text()}\t\t{self.lineedit25.text()}')
    
    
    def send(self):
        pass
    
    
    def edit(self):
        if self.lineedit1.text() != 'Ali':
            self.label1.setText(self.lineedit1.text())

        if self.lineedit2.text() != 'Alizade':
            self.label2.setText(self.lineedit2.text())

        if self.lineedit3.text() != 'Ap 4002':
            self.label3.setText(self.lineedit3.text())

        if self.lineedit4.text() != 'Area 12':
            self.label4.setText(self.lineedit4.text())

        if self.lineedit5.text() != 'Coffe Shop':
            self.label5.setText(self.lineedit5.text())

        if self.lineedit6.text() != 'iran university of science and technology':
            self.label6.setText(self.lineedit6.text())

app = QApplication(sys.argv)
window  = ManagerProfile()
widget=QtWidgets.QStackedWidget()
widget.addWidget(window)
widget.setFixedWidth(1261)
widget.setFixedHeight(881)
widget.show()
app.exec_()