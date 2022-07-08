# import different libraries and files
from PyQt5 import QtWidgets, uic , QtGui,QtCore 
from PyQt5.QtWidgets import QMainWindow ,QApplication ,QPushButton, QFrame, QLabel, QLineEdit, QTableWidget, QAbstractButton, QListWidget, QCalendarWidget, QMessageBox, QCheckBox, QTextEdit, QTableWidgetItem, QComboBox, QDateEdit, QSpinBox
import sys
import random
import smtplib
import time
import sqlite3
from login_db import query
from db_customer_profile import Profile
from db_customer_login import extract_national_code
import re
from db_food_order import insert_table_food, previous_order, confriming_order, confirmation
from datetime import date, datetime
from db_admin_login import *
from db_update_menu import decrease, inventory, insert_table_food_new, update_price_table_food, increase
from vote import insert_table_vote, votes


# Creating FirstPage Class and defining the objects in it.
class FirstPage(QMainWindow):
    def __init__(self):
        super(FirstPage, self).__init__()
        uic.loadUi('firstpage.ui', self)
        self.button = self.findChild(QPushButton, 'managerbutton')
        self.button2 = self.findChild(QPushButton, 'customerbutton')
        self.button.clicked.connect(self.manager)
        self.button2.clicked.connect(self.customer)

    # For choosing to go to the page as a manager.
    def manager(self):
        managerlog = ManagerLogin()
        widget.addWidget(managerlog)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    # For choosing to go to the page as a customer.
    def customer(self):
        customerlog = CustomerLogin()
        widget.addWidget(customerlog)
        widget.setCurrentIndex(widget.currentIndex()+1)


# Creating ManagerLogin Class and defining the objects in it.
class ManagerLogin(QMainWindow):
    def __init__(self):
        super(ManagerLogin, self).__init__()
        uic.loadUi('manager_login.ui', self)
        self.setWindowTitle("ManagerLogin")
        
        self.button = self.findChild(QPushButton, 'pushButton')
        self.button2 = self.findChild(QPushButton, 'pushButton_2')
        self.button.clicked.connect(self.managerlog)
        self.button2.clicked.connect(self.back)
        self.Password.setEchoMode(QLineEdit.Password)
        
    # defining function for back button
    def back(self):
        firstt = FirstPage()
        widget.addWidget(firstt)
        widget.setCurrentIndex(widget.currentIndex()+1)

    # defining function for open main page
    def managerlog(self):
        usernam = self.Username.text()
        passw = self.Password.text()
        # Using The Mentors Email and random Password as a default username and password. 
        if usernam == 'mahdihosseinizade2000@gmail.com' and passw == 'mahdi2000':
            customerlog = ManagerProfile()
            widget.addWidget(customerlog)
            widget.setCurrentIndex(widget.currentIndex()+1)


# Creating CustomerLogin Class and defining the objects in it.
class CustomerLogin(QMainWindow):
    def __init__(self):
        super(CustomerLogin, self).__init__()
        uic.loadUi('customer_login.ui', self)
        
        self.button1 = self.findChild(QPushButton, 'CustomerLogin')
        self.button2 = self.findChild(QPushButton, 'CustomerSignup')
        self.button3 = self.findChild(QPushButton, 'ForgerPass')
        self.emaillineedit = self.findChild(QLineEdit, 'Username')
        self.passline = self.findChild(QLineEdit, 'Password')
        self.passline.setEchoMode(QLineEdit.Password)
        self.button4 = self.findChild(QPushButton, 'CustomerSignup_2')
        self.button1.clicked.connect(self.customerlog)
        self.button2.clicked.connect(self.customersu)
        self.button3.clicked.connect(self.forgetpassword)
        self.button4.clicked.connect(self.back)
        self.checkboxx = self.findChild(QCheckBox, 'checkBox')
        
        self.checkboxx.stateChanged.connect(self.showpass)
        
    # A Method for checkbox to show password. 
    def showpass(self):
        self.Password.setEchoMode(QLineEdit.Normal)

    # Function for a back button.
    def back(self):
        first = FirstPage()
        widget.addWidget(first)
        widget.setCurrentIndex(widget.currentIndex()+1)


    # defining function for open main page
    def customerlog(self):
        res = []
        res.append(self.emaillineedit.text())
        res.append(self.passline.text())
        
       
        if res[0] != '' and res[1] != '':
            names = query(self.emaillineedit.text(), self.passline.text())
            if names == "not exist":
                msg = QMessageBox()
                msg.setText('Error')
                msg.exec_()
            elif names == False:
                msg2 = QMessageBox()
                msg2.setText('Username or Password is wrong!')
                msg2.exec_()
            else:
                global em
                em = self.emaillineedit.text() 
                customerpro = CustomerProfile()
                widget.addWidget(customerpro)
                widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            print('its bad')

    # Defining a function for sign up button.
    def customersu(self):
        customersign = CustomerSignup()
        widget.addWidget(customersign)
        widget.setCurrentIndex(widget.currentIndex()+1)


    # if you forget your password when you push forget password button, it will send you some random password to your email.
    def forgetpassword(self):
        recovery_password = random.randint(1001, 10000)
        smtplib_obj = smtplib.SMTP("smtp.gmail.com", 587)
        smtplib_obj.ehlo()
        smtplib_obj.starttls()
        smtplib_obj.login("AP4002Group4@gmail.com", "rginclqnytypwofj")
        smtplib_obj.sendmail("AP4002Group4@gmail.com", f"{self.emaillineedit}", f"Subject:Password recovery\n{recovery_password}")
        smtplib_obj.quit()
        

# Creating CustomerLogin Class and defining the objects in it.
class ManagerProfile(QMainWindow):
    def __init__(self):
        super(ManagerProfile, self).__init__()
        uic.loadUi('manager_profile.ui', self)
        data = info_admin()
        self.lineedit1 = self.findChild(QLineEdit, 'lineEdit')
        self.lineedit2 = self.findChild(QLineEdit, 'lineEdit_2')
        self.lineedit3 = self.findChild(QLineEdit, 'lineEdit_3')
        self.lineedit4 = self.findChild(QLineEdit, 'lineEdit_5')
        self.lineedit5 = self.findChild(QLineEdit, 'lineEdit_4')
        self.lineedit6 = self.findChild(QLineEdit, 'lineEdit_22')
        self.label1 = self.findChild(QLabel, 'label_63')
        self.label1.setText(data[2])
        self.label2 = self.findChild(QLabel, 'label_66')
        self.label2.setText(data[3])
        self.label3 = self.findChild(QLabel, 'label_65')
        self.label3.setText(data[4])
        self.label4 = self.findChild(QLabel, 'label_64')
        self.label4.setText(data[5])
        self.label5 = self.findChild(QLabel, 'label_67')
        self.label5.setText(data[6])
        self.label6 = self.findChild(QLabel, 'label_68')
        self.label6.setText(data[7])
        self.button = self.findChild(QPushButton, 'pushButton_7')
        self.add_button = self.findChild(QPushButton, 'pushButton_4')
        self.send_discount = self.findChild(QPushButton, 'pushButton_2')
        self.edit_menu = self.findChild(QPushButton, 'pushButton_5')
        self.button.clicked.connect(self.edit)
        self.add_button.clicked.connect(self.add)
        self.send_discount.clicked.connect(self.send)
        self.edit_menu.clicked.connect(self.editing_menu)
       
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

        self.button1 = self.findChild(QPushButton, 'pushButton_8')
        self.button2 = self.findChild(QPushButton, 'pushButton')
        self.button3 = self.findChild(QPushButton, 'pushButton_9')
        self.button1.clicked.connect(self.refresh)
        self.button2.clicked.connect(self.confirm)
        self.button3.clicked.connect(self.showvote)


    # this method will send cutomers discount codes
    def send(self):
        code_part1 = random.choice(['uta', 'utb', 'utc', 'ute', 'utf']) 
        code_part2 = random.randint(1000, 100000)
        final_code = str(code_part1) + str(code_part2)
        
        smtplib_obj = smtplib.SMTP("smtp.gmail.com", 587)
        smtplib_obj.ehlo()
        smtplib_obj.starttls()
        
        smtplib_obj.login("AP4002Group4@gmail.com", "xebtkitiubkazoku")
        smtplib_obj.sendmail("AP4002Group4@gmail.com", f"{extract_national_code(em)[3]}", f"Subject:discount code\n{final_code}")
        smtplib_obj.quit()


    def refresh(self):
        self.tableWidget = self.findChild(QTableWidget, 'tableWidget')
        self.tableWidget.setHorizontalHeaderLabels(['Name', 'Count', 'Date'])
        nat = confriming_order()
        self.tableWidget.setRowCount(len(nat))      
        self.tableWidget.setColumnCount(4)
        for key, nats in enumerate(nat):
            self.tableWidget.setItem(key,0, QTableWidgetItem(nats[1]))         
            self.tableWidget.setItem(key,1, QTableWidgetItem(f"{nats[2]}"))         
            self.tableWidget.setItem(key,2, QTableWidgetItem(nats[3]))
            self.tableWidget.setItem(key,3, QTableWidgetItem(nats[4]))

    def confirm(self):
        confirmation()
        self.tableWidget = self.findChild(QTableWidget, 'tableWidget')
        self.tableWidget.setHorizontalHeaderLabels(['Name', 'Count', 'Date', 'Status'])
        nat = confriming_order()
        self.tableWidget.setRowCount(len(nat))      
        self.tableWidget.setColumnCount(4)
        for key, nats in enumerate(nat):
            self.tableWidget.setItem(key,0, QTableWidgetItem(nats[1]))         
            self.tableWidget.setItem(key,1, QTableWidgetItem(f"{nats[2]}"))         
            self.tableWidget.setItem(key,2, QTableWidgetItem(nats[3]))
            self.tableWidget.setItem(key,3, QTableWidgetItem(nats[4]))
        msg = QMessageBox()
        msg.setText("The Orders will send to their destinations!")
        msg.exec_()


    def editing_menu(self):
        try:
            name2 = self.findChild(QComboBox, "comboBox_2").currentText()
            count2 = self.findChild(QSpinBox, "spinBox_4").value()
            date2 = self.findChild(QDateEdit, "dateEdit_2").date().toPyDate()
            price2 = self.findChild(QSpinBox, "spinBox_3").value()
            update_price_table_food(str(name2) , str(count2) , str(date2) , str(price2))
            if count2 > 0:
                increase((name2) , (count2) , (date2))
                msg = QMessageBox()
                msg.setText("Succesfully Added!")
                msg.exec_()
        except Exception as e:
            print(e)


    def add(self):
        try:
            name = self.findChild(QComboBox, "comboBox").currentText()
            count = self.findChild(QSpinBox, "spinBox").value()
            date = self.findChild(QDateEdit, "dateEdit").date().toPyDate()
            price = self.findChild(QSpinBox, "spinBox_2").value()
            insert_table_food_new(str(name) , str(count) , str(date) , str(price))
            msg = QMessageBox()
            msg.setText("Succesfully Added!")
            msg.exec_()
        except Exception as e:
                print(e)
               
    def showvote(self):
        self.list2 = self.findChild(QListWidget, 'listWidget')
        self.list2.addItem(votes())
    
    
    def edit(self):
        if self.lineedit1.text() != '':
            self.label1.setText(self.lineedit1.text())
            update_table_name(self.lineedit1.text())
            self.lineedit1.setText('')
            

        if self.lineedit2.text() != '':
            self.label2.setText(self.lineedit2.text())
            update_table_family_name(self.lineedit2.text())
            self.lineedit2.setText('')

        if self.lineedit1.text() != '':
            self.label3.setText(self.lineedit3.text())
            update_table_restaurant_name(self.lineedit3.text())
            self.lineedit3.setText('')

        if self.lineedit4.text() != '':
            self.label4.setText(self.lineedit4.text())
            update_table_restaurant_area(self.lineedit4.text())
            self.lineedit4.setText('')

        if self.lineedit5.text() != '':
            self.label5.setText(self.lineedit5.text())
            update_table_restaurant_type(self.lineedit5.text())
            self.lineedit5.setText('')

        if self.lineedit6.text() != '':
            self.label6.setText(self.lineedit6.text())
            update_table_restaurant_address(self.lineedit6.text())
            self.lineedit6.setText('')
        

class CustomerProfile(QMainWindow):
    def __init__(self):
        super(CustomerProfile, self).__init__()
        uic.loadUi('menu_and_customerprofile.ui', self)
        self.button1 = self.findChild(QAbstractButton, 'totalbutton')
        self.button2 = self.findChild(QAbstractButton, 'receiptbutton')
        self.button4 = self.findChild(QAbstractButton, 'orderbutton')
        self.button5 = self.findChild(QAbstractButton, 'resetbutton')
        self.button6 = self.findChild(QAbstractButton, 'cancelbutton')
        self.button7 = self.findChild(QAbstractButton, 'exitbutton')
        self.button8 = self.findChild(QAbstractButton, 'pushButton_6')
        self.button9 = self.findChild(QAbstractButton, 'pushButton_8')
        self.button10 = self.findChild(QAbstractButton, 'pushButton_9')
        self.button11 = self.findChild(QPushButton, 'pushButton_10')
        self.button1.clicked.connect(self.total)
        self.button2.clicked.connect(self.receipt)
        self.button4.clicked.connect(self.order)
        self.button5.clicked.connect(self.reset)
        self.button6.clicked.connect(self.cancel)
        self.button7.clicked.connect(self.exitbutt)
        self.button8.clicked.connect(self.search)
        self.button9.clicked.connect(self.edit)
        self.button10.clicked.connect(self.submit)
        self.button11.clicked.connect(self.refresh)
        self.lineedit = self.findChild(QLineEdit, 'lineEdit_6')
        self.lineedit2 = self.findChild(QLineEdit, 'lineEdit_7')
        self.lineedit3 = self.findChild(QLineEdit, 'lineEdit_8')
        self.lineedit4 = self.findChild(QLineEdit, 'lineEdit_9')
        self.lineedit5 = self.findChild(QLineEdit, 'lineEdit_10')
        self.lineedit6 = self.findChild(QLineEdit, 'lineEdit_11')
        self.lineedit7 = self.findChild(QLineEdit, 'lineEdit_12')
        self.lineedit8 = self.findChild(QLineEdit, 'lineEdit_13')
        self.lineedit9 = self.findChild(QLineEdit, 'lineEdit_14')
        self.lineedit10 = self.findChild(QLineEdit, 'lineEdit_15')
        self.lineedit11 = self.findChild(QLineEdit, 'lineEdit_16')
        self.lineedit12 = self.findChild(QLineEdit, 'lineEdit_17')
        self.lineedit13 = self.findChild(QLineEdit, 'lineEdit_18')
        self.lineedit14 = self.findChild(QLineEdit, 'lineEdit_19')
        self.lineedit15 = self.findChild(QLineEdit, 'lineEdit_20')
        self.lineedit16 = self.findChild(QLineEdit, 'lineEdit_21')
        self.lineedit17 = self.findChild(QLineEdit, 'lineEdit_30')
        self.lineedit18 = self.findChild(QLineEdit, 'lineEdit_22')
        self.lineedit19 = self.findChild(QLineEdit, 'lineEdit_23')
        self.lineedit20 = self.findChild(QLineEdit, 'lineEdit_24')
        self.lineedit21 = self.findChild(QLineEdit, 'lineEdit_25')
        self.lineedit22 = self.findChild(QLineEdit, 'lineEdit_28')
        self.lineedit23 = self.findChild(QLineEdit, 'lineEdit_29')
        self.label = self.findChild(QLabel, 'label_12')
        self.label2 = self.findChild(QLabel, 'label_13')
        self.label3 = self.findChild(QLabel, 'label_14')
        self.label4 = self.findChild(QLabel, 'label_15')
        self.label5 = self.findChild(QLabel, 'label_17')
        self.label6 = self.findChild(QLabel, 'label_18')
        self.label7 = self.findChild(QLabel, 'label_19')
        self.label8 = self.findChild(QLabel, 'label_20')
        self.label9 = self.findChild(QLabel, 'label_22')
        self.label10 = self.findChild(QLabel, 'label_23')
        self.label11 = self.findChild(QLabel, 'label_24')
        self.label12 = self.findChild(QLabel, 'label_25')
        self.label13 = self.findChild(QLabel, 'label_27')
        self.label14 = self.findChild(QLabel, 'label_28')
        self.label15 = self.findChild(QLabel, 'label_29')
        self.label16 = self.findChild(QLabel, 'label_30')
        self.order_list = self.findChild(QListWidget, 'listWidget')
        self.menu = {self.label.text(): 19, self.label2.text(): 16, self.label3.text(): 16, self.label4.text(): 17, self.label5.text(): 36,
        self.label6.text(): 40, self.label7.text(): 39, self.label8.text(): 40, self.label9.text(): 9.5, self.label12.text(): 8.5, 
        self.label10.text(): 5, self.label11.text(): 8, self.label13.text(): 2.5, self.label16.text(): 3.5, self.label14.text(): 2, 
        self.label15.text(): 4}
        self.textt = self.findChild(QListWidget, 'listWidget_2')
        self.textt2 = self.findChild(QListWidget, 'listWidget_3')
        self.calendar = self.findChild(QCalendarWidget, 'calendarWidget')
        self.calendar.selectionChanged.connect(self.calendar_date)
        self.calendar_date()
        self.texteedit = self.findChild(QTextEdit, 'textEdit')
        self.menu_and_count = {self.label.text(): self.lineedit.text(), self.label2.text(): self.lineedit2.text(), self.label3.text(): self.lineedit3.text(), self.label4.text(): self.lineedit4.text(), self.label5.text(): self.lineedit5.text(), self.label6.text(): self.lineedit6.text(), self.label7.text(): self.lineedit7.text(), self.label8.text(): self.lineedit8.text(), self.label9.text(): self.lineedit9.text(), self.label10.text(): self.lineedit10.text(), self.label11.text(): self.lineedit11.text(), self.label12.text(): self.lineedit12.text(), self.label13.text(): self.lineedit13.text(), self.label14.text(): self.lineedit14.text(), self.label15.text(): self.lineedit15.text(), self.label16.text(): self.lineedit16.text()}
 

        self.list1 = self.findChild(QListWidget, 'listWidget')
        ex = extract_national_code(em)
        self.list1.addItem(f'Name: \t\t\t{ex[0]}\n\n')
        self.list1.addItem(f'Family Name: \t\t{ex[1]}\n\n')
        self.list1.addItem(f'Phone Number: \t\t{ex[2]}\n\n')
        self.list1.addItem(f'Email: \t\t{ex[3]}\n\n')
        self.list1.addItem(f'National Number: \t\t{ex[4]}\n\n')
        self.list1.addItem(f'Address: \t\t\t{ex[7]}\n\n')


    def calendar_date(self):
        self.lineedit.setEnabled(False)
        self.lineedit2.setEnabled(False)
        self.lineedit3.setEnabled(False)
        self.lineedit4.setEnabled(False)
        self.lineedit5.setEnabled(False)
        self.lineedit6.setEnabled(False)
        self.lineedit7.setEnabled(False)
        self.lineedit8.setEnabled(False)
        self.lineedit9.setEnabled(False)
        self.lineedit10.setEnabled(False)
        self.lineedit11.setEnabled(False)
        self.lineedit12.setEnabled(False)
        self.lineedit13.setEnabled(False)
        self.lineedit14.setEnabled(False)
        self.lineedit15.setEnabled(False)
        self.lineedit16.setEnabled(False)
        value = self.calendar.selectedDate().toString("yyyy-MM-dd")
        food_list = inventory(value)
        self.textt.clear()
        for food in food_list:
            self.textt.addItem(food['name'] + ": " + str(food['count']))
        
            if food['name'] == "Spicy Lobster":
                self.label.setText(f"𝑺𝒑𝒊𝒄𝒚 𝑳𝒐𝒃𝒔𝒕𝒆𝒓------------------${food['price']}")
                self.lineedit.setEnabled(True)
            
            elif food['name'] == "Baked Escargot":
                self.label2.setText(f"𝑩𝒂𝒌𝒆𝒅 𝑬𝒔𝒄𝒂𝒓𝒈𝒐𝒕--------------${food['price']}")
                self.lineedit2.setEnabled(True)

            elif food['name'] == "Shrimp Cocktail":
                self.label3.setText(f"𝑺𝒉𝒓𝒊𝒎𝒑 𝑪𝒐𝒄𝒌𝒕𝒂𝒊𝒍--------------${food['price']}")
                self.lineedit3.setEnabled(True)

            elif food['name'] == "Seared Ahi Tuna":
                self.label4.setText(f"𝑺𝒆𝒂𝒓𝒆𝒅 𝑨𝒉𝒊 𝑻𝒖𝒏𝒂-------------${food['price']}")
                self.lineedit4.setEnabled(True)

            elif food['name'] == "Filet Mignon, 8ounce":
                self.label5.setText(f"𝑭𝒊𝒍𝒆𝒕 𝑴𝒊𝒈𝒏𝒐𝒏, 𝟖𝒐𝒖𝒏𝒄𝒆-------${food['price']}")
                self.lineedit5.setEnabled(True)

            elif food['name'] == "Filet Mignon, 16ounce":
                self.label6.setText(f"𝑭𝒊𝒍𝒆𝒕 𝑴𝒊𝒈𝒏𝒐𝒏, 𝟏𝟐𝒐𝒖𝒏𝒄𝒆-------${food['price']}")
                self.lineedit6.setEnabled(True)

            elif food['name'] == "Rib Eye Steak, 18ounce":
                self.label7.setText(f"𝑹𝒊𝒃 𝑬𝒚𝒆 𝑺𝒕𝒆𝒂𝒌, 𝟏𝟖 𝒐𝒖𝒏𝒄𝒆----${food['price']}")
                self.lineedit7.setEnabled(True)

            elif food['name'] == "Porterhouse for two":
                self.label8.setText(f"𝑷𝒐𝒓𝒕𝒆𝒓𝒉𝒐𝒖𝒔𝒆 𝒇𝒐𝒓 𝒕𝒘𝒐-------${food['price']}")
                self.lineedit8.setEnabled(True)

            elif food['name'] == "Spinach Salad":
                self.label9.setText(f"𝑺𝒑𝒊𝒏𝒂𝒄𝒉 𝑺𝒂𝒍𝒂𝒅-----------------${food['price']}")
                self.lineedit9.setEnabled(True)

            elif food['name'] == "Caprese Salad":
                self.label10.setText(f"𝑪𝒂𝒑𝒓𝒆𝒔𝒆 𝑺𝒂𝒍𝒂𝒅-----------------${food['price']}")
                self.lineedit11.setEnabled(True)

            elif food['name'] == "French Onion Soup":
                self.label11.setText(f"𝑭𝒓𝒆𝒏𝒄𝒉 𝑶𝒏𝒊𝒐𝒏 𝑺𝒐𝒖𝒑----------${food['price']}")
                self.lineedit11.setEnabled(True)

            elif food['name'] == "Lobster Bisque":
                self.label12.setText(f"𝑳𝒐𝒃𝒔𝒕𝒆𝒓 𝑩𝒊𝒔𝒒𝒖𝒆----------------${food['price']}")
                self.lineedit12.setEnabled(True)
            
            elif food['name'] == "Tea":
                self.label13.setText(f"𝑻𝒆𝒂---------------------------------${food['price']}")
                self.lineedit13.setEnabled(True)
            
            elif food['name'] == "Coffe":
                self.label14.setText(f"𝑪𝒐𝒇𝒇𝒆------------------------------${food['price']}")
                self.lineedit14.setEnabled(True)
            
            elif food['name'] == "Coca":
                self.label15.setText(f"𝑪𝒐𝒄𝒂--------------------------------${food['price']}")
                self.lineedit15.setEnabled(True)
            
            elif food['name'] == "Orange Juice":
                self.label16.setText(f"𝑶𝒓𝒂𝒏𝒈𝒆 𝑱𝒖𝒊𝒄𝒆--------------------4.00${food['price']}")
                self.lineedit16.setEnabled(True)


    def edit(self):
        if self.lineedit18.text() != '':
            ex = extract_national_code(em)
            prof = Profile(ex[4])
            prof.update_table_name(self.lineedit18.text())
            self.lineedit18.setText('')



        if self.lineedit19.text() != '':
            ex2 = extract_national_code(em)
            prof2 = Profile(ex2[4])
            prof2.update_table_family_name(self.lineedit19.text())
            self.lineedit19.setText('')

        
        if self.lineedit20.text() != '':
            ex3 = extract_national_code(em)
            prof3 = Profile(ex3[4])
            prof3.update_table_phone_number(self.lineedit20.text())
            self.lineedit20.setText('')
            

        if self.lineedit22.text() != '':
            ex5 = extract_national_code(em)
            prof5 = Profile(ex5[4])
            prof5.update_table_password(self.lineedit22.text())
            self.lineedit22.setText('')
            
        
        if self.lineedit21.text() != '':
            ex7 = extract_national_code(em)
            prof7 = Profile(ex7[4])
            prof7.update_table_repeat_pass(self.lineedit21.text())
            self.lineedit21.setText('')

        
        if self.lineedit23.text() != '':
            ex6 = extract_national_code(em)
            prof6 = Profile(ex6[4])
            prof6.update_table_email(self.lineedit23.text())
            self.lineedit23.setText('')
            


        msg = QMessageBox()
        msg.setText("Succesfull!!")
        msg.exec_()


    def submit(self):
        if self.texteedit.toPlainText() != '':
            insert_table_vote(self.texteedit.toPlainText())
            msg = QMessageBox()
            msg.setText("Thanks for your help!!")
            msg.exec_()

    def search(self):
        value = self.calendar.selectedDate().toString("yyyy-MM-dd")
        food_list = inventory(value)
        self.textt.clear()
        for food in food_list:
            if food['name'] == self.lineedit17.text():
                self.textt.addItem(food['name'] + ": " + str(food['count']))


    
    def total(self):
        total_list = []
        result = []
        total_list.append(self.lineedit.text())
        total_list.append(self.lineedit2.text())
        total_list.append(self.lineedit3.text())
        total_list.append(self.lineedit4.text())
        total_list.append(self.lineedit5.text())
        total_list.append(self.lineedit6.text())
        total_list.append(self.lineedit7.text())
        total_list.append(self.lineedit8.text())
        total_list.append(self.lineedit9.text())
        total_list.append(self.lineedit10.text())
        total_list.append(self.lineedit11.text())
        total_list.append(self.lineedit12.text())
        total_list.append(self.lineedit13.text())
        total_list.append(self.lineedit14.text())
        total_list.append(self.lineedit15.text())
        total_list.append(self.lineedit16.text())
        
        for tot in total_list:
            try:
                z = int(tot)
                result.append(z)
            except:
                result.append(0)
        a = result[0] * self.menu[self.label.text()]
        b = result[1] * self.menu[self.label2.text()]
        c = result[2] * self.menu[self.label3.text()]
        d = result[3] * self.menu[self.label4.text()]
        e = result[4] * self.menu[self.label5.text()]
        f = result[5] * self.menu[self.label6.text()]
        g = result[6] * self.menu[self.label7.text()]
        h = result[7] * self.menu[self.label8.text()]
        i = result[8] * self.menu[self.label9.text()]
        j = result[9] * self.menu[self.label12.text()]
        k = result[10] * self.menu[self.label10.text()]
        l = result[11] * self.menu[self.label11.text()]
        m = result[12] * self.menu[self.label13.text()]
        n = result[13] * self.menu[self.label16.text()]
        o = result[14] * self.menu[self.label14.text()]
        p = result[15] * self.menu[self.label15.text()]
        self.textt2.addItem(f'${str(a + b + c + d + e + f + g + h + i + j + k + l + m + n + o + p)}')

    def receipt(self):
        total_list = []
        result = []
        total_list.append(self.lineedit.text())
        total_list.append(self.lineedit2.text())
        total_list.append(self.lineedit3.text())
        total_list.append(self.lineedit4.text())
        total_list.append(self.lineedit5.text())
        total_list.append(self.lineedit6.text())
        total_list.append(self.lineedit7.text())
        total_list.append(self.lineedit8.text())
        total_list.append(self.lineedit9.text())
        total_list.append(self.lineedit10.text())
        total_list.append(self.lineedit11.text())
        total_list.append(self.lineedit12.text())
        total_list.append(self.lineedit13.text())
        total_list.append(self.lineedit14.text())
        total_list.append(self.lineedit15.text())
        total_list.append(self.lineedit16.text())
        
        for tot in total_list:
            try:
                z = int(tot)
                result.append(z)
            except:
                result.append(0)
        a = result[0] * self.menu[self.label.text()]
        b = result[1] * self.menu[self.label2.text()]
        c = result[2] * self.menu[self.label3.text()]
        d = result[3] * self.menu[self.label4.text()]
        e = result[4] * self.menu[self.label5.text()]
        f = result[5] * self.menu[self.label6.text()]
        g = result[6] * self.menu[self.label7.text()]
        h = result[7] * self.menu[self.label8.text()]
        i = result[8] * self.menu[self.label9.text()]
        j = result[9] * self.menu[self.label12.text()]
        k = result[10] * self.menu[self.label10.text()]
        l = result[11] * self.menu[self.label11.text()]
        m = result[12] * self.menu[self.label13.text()]
        n = result[13] * self.menu[self.label16.text()]
        o = result[14] * self.menu[self.label14.text()]
        p = result[15] * self.menu[self.label15.text()]
        date = time.strftime('%d/%m/%Y')
        myFile = open('Receipt.txt', 'w')
        myFile.write(date + '\n')
        myFile.write('ITEMS\t\t\t\tQUANTITY\tPRICE\n')
        myFile.write('----------------------------------------------------------\n')

        if result[0] == 0 and result[1] == 0 and result[2] == 0 and result[3] == 0 and result[4] == 0 and result[5] == 0 and result[6] == 0 and result[7] == 0 and result[8] == 0 and result[9] == 0 and result[10] == 0 and result[11] == 0 and result[12] == 0 and result[13] == 0 and result[14] == 0 and result[15] == 0:
            msg = QMessageBox()
            msg.setText('You must order something!')
            msg.exec_()

        if result[0] != 0:
            myFile.write(f"Spicy Lobster\t\t{total_list[0]}\t\t{int(result[0])*19}\n")
            
        if result[1] != 0:
            myFile.write(f"Baked Scargot\t\t{total_list[1]}\t\t{int(result[1])*16}\n")

        if result[2] != 0:
            myFile.write(f"Shrimp Cocktail\t\t{total_list[2]}\t\t{int(result[2])*16}\n")

        if result[3] != 0:
            myFile.write(f"Seared Ahi Tuna\t\t{total_list[3]}\t\t{int(result[3])*17}\n")

        if result[4] != 0:
            myFile.write(f"Filet Mignon, 8ounce\t\t{total_list[4]}\t\t{int(result[4])*36}\n")

        if result[5] != 0:
            myFile.write(f"Filet Mignon, 12ounce\t\t{total_list[5]}\t\t{int(result[5])*40}\n")

        if result[6] != 0:
            myFile.write(f"Rib Eye Steak, 18ounce\t\t{total_list[6]}\t\t{int(result[6])*39}\n")

        if result[7] != 0:
            myFile.write(f"Porterhouse For Two\t\t{total_list[7]}\t\t{int(result[7])*40}\n")

        if result[8] != 0:
            myFile.write(f"Spinach Salad\t\t{total_list[8]}\t\t{float(result[8])*9.5}\n")

        if result[9] != 0:
            myFile.write(f"Caprese Salad\t\t{total_list[9]}\t\t{float(result[9])*8.5}\n")

        if result[10] != 0:
            myFile.write(f"French Onion Soup\t\t{total_list[10]}\t\t{int(result[10])*5}\n")
            self.order_list.addItem(f"French Onion Soup\t\t{total_list[10]}\t\t{int(result[10])*5}\n")

        if result[11] != 0:
            myFile.write(f"Lobster Bisque\t\t{total_list[11]}\t\t{int(result[11])*8}\n")

        if result[12] != 0:
            myFile.write(f"Tea\t\t\t\t\t{total_list[12]}\t\t\t\t{float(result[12])*2.5}\n")
        
        if result[13] != 0:    
            myFile.write(f"Coffe\t\t\t\t{total_list[13]}\t\t\t\t{float(result[13])*3.5}\n")

        if result[14] != 0:
            myFile.write(f"Coca\t\t{total_list[14]}\t\t{int(result[14])*2}\n")

        if result[15] != 0:
            myFile.write(f"Orange Juice\t\t\t{total_list[15]}\t\t\t{int(result[15])*4}\n")


        myFile.write(f'TOTAL : ${a + b + c + d + e + f + g + h + i + j + k + l + m + n + o + p}')
        myFile.close()


    def order(self):
        total_list = []
        result = []
        total_list.append(self.lineedit.text())
        total_list.append(self.lineedit2.text())
        total_list.append(self.lineedit3.text())
        total_list.append(self.lineedit4.text())
        total_list.append(self.lineedit5.text())
        total_list.append(self.lineedit6.text())
        total_list.append(self.lineedit7.text())
        total_list.append(self.lineedit8.text())
        total_list.append(self.lineedit9.text())
        total_list.append(self.lineedit10.text())
        total_list.append(self.lineedit11.text())
        total_list.append(self.lineedit12.text())
        total_list.append(self.lineedit13.text())
        total_list.append(self.lineedit14.text())
        total_list.append(self.lineedit15.text())
        total_list.append(self.lineedit16.text())
        
        for tot in total_list:
            try:
                z = int(tot)
                result.append(z)
            except:
                result.append(0)
        ex = extract_national_code(em)[4]

        if result[0] == 0 and result[1] == 0 and result[2] == 0 and result[3] == 0 and result[4] == 0 and result[5] == 0 and result[6] == 0 and result[7] == 0 and result[8] == 0 and result[9] == 0 and result[10] == 0 and result[11] == 0 and result[12] == 0 and result[13] == 0 and result[14] == 0 and result[15] == 0:
            msg = QMessageBox()
            msg.setText('You must order something!')
            msg.exec_()

        value = self.calendar.selectedDate().toString("yyyy-MM-dd")
        if result[0] != 0:
            insert_table_food(ex, 'Spicy Lobster', result[0], value)
            decrease('Spicy Lobster', result[0], value)
            
        if result[1] != 0:
            insert_table_food(ex, 'Baked Scargot', result[1], datetime.today().strftime('%Y-%m-%d'))
            decrease('Baked Scargot', result[1], value)

        if result[2] != 0:
            insert_table_food(ex, 'Shrimp Cocktail', result[2], datetime.today().strftime('%Y-%m-%d'))
            decrease('Shrimp Cocktail', result[2], value)

        if result[3] != 0:
            insert_table_food(ex, 'Seared Ahi Tuna', result[3], datetime.today().strftime('%Y-%m-%d'))
            decrease('Seared Ahi Tuna', result[3], value)

        if result[4] != 0:
            insert_table_food(ex, 'Filet Mignon, 8ounce', result[4], datetime.today().strftime('%Y-%m-%d'))
            decrease('Filet Mignon, 8ounce', result[4], value)

        if result[5] != 0:
            insert_table_food(ex, 'Filet Mignon, 12ounce', result[5], datetime.today().strftime('%Y-%m-%d'))
            decrease('Filet Mignon, 12ounce', result[5], value)

        if result[6] != 0:
            insert_table_food(ex, 'Rib Eye Steak, 18ounce', result[6], datetime.today().strftime('%Y-%m-%d'))
            decrease('Rib Eye Steak, 18ounce', result[6], value)

        if result[7] != 0:
            insert_table_food(ex, 'Porterhouse For Two', result[7], datetime.today().strftime('%Y-%m-%d'))
            decrease('Porterhouse For Two', result[7], value)

        if result[8] != 0:
            insert_table_food(ex, 'Spinach Salad', result[8], datetime.today().strftime('%Y-%m-%d'))
            decrease('Spinach Salad', result[8], value)

        if result[9] != 0:
            insert_table_food(ex, 'Caprese Salad', result[9], datetime.today().strftime('%Y-%m-%d'))
            decrease('Caprese Salad', result[9], value)

        if result[10] != 0:
            insert_table_food(ex, 'French Onion Soup', result[10], datetime.today().strftime('%Y-%m-%d'))
            decrease('French Onion Soup', result[10], value)

        if result[11] != 0:
            insert_table_food(ex, 'Lobster Bisque', result[11], datetime.today().strftime('%Y-%m-%d'))
            decrease('Lobster Bisque', result[11], value)

        if result[12] != 0:
            insert_table_food(ex, 'Tea', result[12], datetime.today().strftime('%Y-%m-%d'))
            decrease('Tea', result[12], value)

        if result[13] != 0:
            insert_table_food(ex, 'Coffe', result[13], datetime.today().strftime('%Y-%m-%d'))    
            decrease('Coffe', result[13], value)

        if result[14] != 0:
            insert_table_food(ex, 'Coca', result[14], datetime.today().strftime('%Y-%m-%d'))
            decrease('Coca', result[14], value)

        if result[15] != 0:
            insert_table_food(ex, 'Orange Juice', result[15], datetime.today().strftime('%Y-%m-%d'))
            decrease('Orange Juice', result[15], value)

        paymenttt = Paymnet()
        widget.addWidget(paymenttt)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def refresh(self):
        self.tableWidget = self.findChild(QTableWidget, 'tableWidget')
        self.tableWidget.setHorizontalHeaderLabels(['Name', 'Count', 'Date', 'Status'])
        nat = previous_order(extract_national_code(em)[4])
        self.tableWidget.setRowCount(len(nat))        
        self.tableWidget.setColumnCount(4)
        for key, nats in enumerate(nat):
            self.tableWidget.setItem(key,0, QTableWidgetItem(nats[1]))         
            self.tableWidget.setItem(key,1, QTableWidgetItem(f"{nats[2]}"))         
            self.tableWidget.setItem(key,2, QTableWidgetItem(nats[3]))
            self.tableWidget.setItem(key,3, QTableWidgetItem(nats[4]))
        


    def reset(self):
        self.lineedit.clear()
        self.lineedit2.clear()
        self.lineedit3.clear()
        self.lineedit4.clear()
        self.lineedit5.clear()
        self.lineedit6.clear()
        self.lineedit7.clear()
        self.lineedit8.clear()
        self.lineedit9.clear()
        self.lineedit10.clear()
        self.lineedit11.clear()
        self.lineedit12.clear()
        self.lineedit13.clear()
        self.lineedit14.clear()
        self.lineedit15.clear()
        self.lineedit16.clear()


    def cancel(self):
        qm = QMessageBox()
        ret = qm.question(self,'', "Are you sure?", qm.Yes | qm.No)
        if ret == qm.Yes:
            self.close()

        else:
            qm.information(self,'',"Nothing Changed")


    def exitbutt(self):
        self.close()



class Paymnet(QMainWindow):
    def __init__(self):
        super(Paymnet, self).__init__()
        uic.loadUi("payment.ui", self)

        self.button = self.findChild(QPushButton, 'CustomerLogin')
        self.button2 = self.findChild(QPushButton, 'CustomerLogin_2')
        self.button3 = self.findChild(QPushButton, 'CustomerLogin_3')


        self.button.clicked.connect(self.online)
        self.button2.clicked.connect(self.home)
        self.button3.clicked.connect(self.back)


    def online(self):
        onlinepayy = OnlinePay()
        widget.addWidget(onlinepayy)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        

    def home(self):
        msg = QMessageBox()
        msg.setText("You will pay cash on delivery!!")
        msg.setWindowTitle("Payment")
        msg.exec_()

    def back(self):
        backk = CustomerProfile()
        widget.addWidget(backk)
        widget.setCurrentIndex(widget.currentIndex()+1)

class OnlinePay(QMainWindow):
    def __init__(self):
        super(OnlinePay, self).__init__()
        uic.loadUi('onlinepayment.ui', self)
        self.button = self.findChild(QPushButton, 'CustomerLogin_2')
        self.button2 = self.findChild(QPushButton, 'CustomerLogin_3')
        self.button.clicked.connect(self.pay)
        self.button2.clicked.connect(self.back)

    def pay(self):
        msg = QMessageBox()
        msg.setText("Succesfull!!")
        msg.setWindowTitle("Online Payment")
        msg.exec_()

    def back(self):
        back = CustomerProfile()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)

class CustomerSignup(QMainWindow):
    result = []
    def __init__(self):
        
        super(CustomerSignup, self).__init__()
        uic.loadUi('customer_signup.ui', self)
        self.button = self.findChild(QPushButton, 'pushButton')
        self.button2 = self.findChild(QPushButton, 'pushButton_2')
        self.button.clicked.connect(self.back_costumerlog)
        self.button2.clicked.connect(self.back_button)

        self.lineedit1 = self.findChild(QLineEdit, 'lineEdit_17')
        self.lineedit2 = self.findChild(QLineEdit, 'lineEdit')
        self.lineedit3 = self.findChild(QLineEdit, 'email_lineedit')
        self.lineedit4 = self.findChild(QLineEdit, 'lineEdit_3')
        self.lineedit5 = self.findChild(QLineEdit, 'lineEdit_4')
        self.lineedit6 = self.findChild(QLineEdit, 'lineEdit_2')
        self.lineedit7 = self.findChild(QLineEdit, 'lineEdit_5')
        self.lineedit8 = self.findChild(QLineEdit, 'lineEdit_6')

        self.validate_name = '^[a-zA-Z]+$'
        self.validate_family_name = '^[a-zA-Z]+$'
        self.valid_phone_number1 = re.compile(r'09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}')
        self.valid_phone_number2 = re.compile(r'9(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}')
        self.valid_phone_number3 = re.compile(r'(\+98)?9\d{9}')
        self.valid_phone_number4 = re.compile(r'00989(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}')
        self.validate_email = '^[a-zA-Z0-9\.\_]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
        self.validate_national_code = '^[0-9]{10}$'
        self.validate_address = '^[a-zA-Z0-9]+$'
        self.validate_password = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
        self.validate_reppassword = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"

    def back_costumerlog(self):
        db_res = []
        a = (self.lineedit1.text(), self.lineedit2.text(), self.lineedit4.text(), self.lineedit3.text(), self.lineedit5.text(), self.lineedit7.text(), self.lineedit8.text(), self.lineedit6.text())
        db_res.append(a)
        CustomerSignup.result.append(self.lineedit1.text())
        CustomerSignup.result.append(self.lineedit2.text())
        CustomerSignup.result.append(self.lineedit3.text())
        CustomerSignup.result.append(self.lineedit4.text())
        CustomerSignup.result.append(self.lineedit5.text())
        CustomerSignup.result.append(self.lineedit6.text())
        CustomerSignup.result.append(self.lineedit7.text())
        CustomerSignup.result.append(self.lineedit8.text())
        
        if CustomerSignup.result[0] != '' and CustomerSignup.result[1] != '' and CustomerSignup.result[2] != '' and CustomerSignup.result[3] != '' and CustomerSignup.result[4] != '' and CustomerSignup.result[5] != '' and CustomerSignup.result[6] != '' and CustomerSignup.result[7] != '':
            
            
            if re.match(self.validate_name, self.lineedit1.text()) and re.match(self.validate_family_name, self.lineedit2.text()) and re.match(self.validate_email, self.lineedit3.text()) and (re.match(self.valid_phone_number1, self.lineedit4.text()) or re.match(self.valid_phone_number2, self.lineedit4.text()) or re.match(self.valid_phone_number3, self.lineedit4.text()) or re.match(self.valid_phone_number4, self.lineedit4.text())) and re.match(self.validate_national_code, self.lineedit5.text()) and re.match(self.validate_address, self.lineedit6.text()) and re.match(self.validate_password, self.lineedit7.text()) and re.match(self.validate_reppassword, self.lineedit8.text()):
                
                conn = sqlite3.connect('customer.db')
                c = conn.cursor()
                c.execute('''CREATE TABLE IF NOT EXISTS customers
                (name text NOT NULL,
                family_name text NOT NULL, 
                phone_number integer NOT NULL, 
                email text NOT NULL, 
                national_code integer NOT NULL, 
                password text NOT NULL, 
                repeat_password text NOT NULL,
                adress text NOT NULL
                    )''')
                c.executemany("INSERT INTO customers VALUES(?, ?, ?, ?, ?, ?, ?, ?)", db_res)
                conn.commit()
                conn.close()
                back_cl = CustomerLogin()
                widget.addWidget(back_cl)
                widget.setCurrentIndex(widget.currentIndex()+1)

            if not re.match(self.validate_name, self.lineedit1.text()):
                msg = QMessageBox()
                msg.setText('The name field must not have anything except uppercase and lowercase letters!!')
                msg.exec_()

            if not re.match(self.validate_family_name, self.lineedit2.text()):
                msg2 = QMessageBox()
                msg2.setText('The familyname field must not have anything except uppercase and lowercase letters!!')
                msg2.exec_()

            if not re.match(self.validate_email, self.lineedit3.text()):
                msg3 = QMessageBox()
                msg3.setText('The format of your email address should be like this : XYZ@A.B')
                msg3.exec_()

            if not re.match(self.valid_phone_number1, self.lineedit4.text()) and not re.match(self.valid_phone_number2, self.lineedit4.text()) and not re.match(self.valid_phone_number3, self.lineedit4.text()) and not re.match(self.valid_phone_number4, self.lineedit4.text()):
                msg4 = QMessageBox()
                msg4.setText('The format of Phone number should be like this:  +9812 or 0912 or 0098912 or 912')
                msg4.exec_()

            if not re.match(self.validate_national_code, self.lineedit5.text()):
                msg5 = QMessageBox()
                msg5.setText('The national code must have 10-digit!')
                msg5.exec_()

            if not re.match(self.validate_address, self.lineedit6.text()):
                msg6 = QMessageBox()
                msg6.setText('The address should at least be the name of a place!!')
                msg6.exec_()

            if not re.match(self.validate_password, self.lineedit7.text()):
                msg7 = QMessageBox()
                msg7.setText('The password must have lowecase and uppercase letters and also have letters like @, # or sth like that!')
                msg7.exec_()
        else:
            self.button.setEnabled(False)
            time.sleep(5)
            self.button.setEnabled(True)

    def back_button(self):
        back_butt = CustomerLogin()
        widget.addWidget(back_butt)
        widget.setCurrentIndex(widget.currentIndex()+1)

app = QApplication(sys.argv)
window  = FirstPage()
widget=QtWidgets.QStackedWidget()
widget.addWidget(window)
widget.setFixedWidth(1261)
widget.setFixedHeight(881)
widget.show()
app.exec_()