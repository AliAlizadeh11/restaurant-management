from PyQt5 import QtWidgets, uic , QtGui,QtCore 
from PyQt5.QtWidgets import QMainWindow ,QApplication ,QPushButton, QFrame, QLabel, QLineEdit, QTableWidget, QAbstractButton, QMessageBox, QListWidget, QCalendarWidget
from PyQt5.QtGui import QFont
import sys
import time



class CustomerProfile(QMainWindow):
   
    def __init__(self):
        super(CustomerProfile, self).__init__()
        uic.loadUi("menu_and_customerprofile.ui", self)
        self.tab1 = self.findChild(QTableWidget, 'menutab')
        self.tab2 = self.findChild(QTableWidget, 'profiletab')
        self.tab3 = self.findChild(QTableWidget, 'editprofiletab')
        self.tab4 = self.findChild(QTableWidget, 'ordertab')
        self.tab5 = self.findChild(QTableWidget, 'helptab')
        self.button1 = self.findChild(QAbstractButton, 'totalbutton')
        self.button2 = self.findChild(QAbstractButton, 'receiptbutton')
        self.button3 = self.findChild(QAbstractButton, 'downloadbutton')
        self.button4 = self.findChild(QAbstractButton, 'orderbutton')
        self.button5 = self.findChild(QAbstractButton, 'resetbutton')
        self.button6 = self.findChild(QAbstractButton, 'cancelbutton')
        self.button7 = self.findChild(QAbstractButton, 'exitbutton')
        self.button8 = self.findChild(QAbstractButton, 'pushButton_6')
        self.button9 = self.findChild(QAbstractButton, 'pushButton_8')
        self.button10 = self.findChild(QAbstractButton, 'pushButton_9')
        self.button1.clicked.connect(self.total)
        self.button2.clicked.connect(self.receipt)
        self.button3.clicked.connect(self.download)
        self.button4.clicked.connect(self.order)
        self.button5.clicked.connect(self.reset)
        self.button6.clicked.connect(self.cancel)
        self.button7.clicked.connect(self.exitbutt)
        self.button8.clicked.connect(self.search)
        self.button9.clicked.connect(self.edit)
        self.button10.clicked.connect(self.submit)
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
        self.menu = {self.label.text(): 19, self.label2.text(): 16, self.label3.text(): 16, self.label4.text(): 17, self.label5.text(): 36,
        self.label6.text(): 40, self.label7.text(): 39, self.label8.text(): 40, self.label9.text(): 9.5, self.label12.text(): 8.5, 
        self.label10.text(): 5, self.label11.text(): 8, self.label13.text(): 2.5, self.label16.text(): 3.5, self.label14.text(): 2, 
        self.label15.text(): 4}
        self.textt = self.findChild(QListWidget, 'listWidget_2')
        self.textt2 = self.findChild(QListWidget, 'listWidget_3')
        self.textt.setFont(QFont('Arial', 10))
        self.calendar = self.findChild(QCalendarWidget, 'calendarWidget')
        self.calendar.selectionChanged.connect(self.calendar_date)
        


    def calendar_date(self):
        
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
        count1 = 20
        count2 = 20
        count3 = 20
        count4 = 20
        count5 = 20
        count6 = 20
        count7 = 20
        count8 = 20
        count9 = 20
        count10 = 20
        count11 = 20
        count12 = 20
        count13 = 20
        count14 = 20
        count15 = 20
        count16 = 20

        self.calendar.selectedDate()
        self.textt.clear()
        self.textt.addItem(f'Spicy Lobster: {count1}\nBaked Scargot: {count2}\nShrimp Cocktail: {count3}\nSeaRed Ahi Tuna: {count4}\nFilet Mignon, 8ounce: {count5}\nFilet Mignon, 12ounce: {count6}\nRib Eye Steak, 18ounce: {count7}\nPorter house for two: {count8}\nSpinach Salad: {count9}\nCaprese Salad: {count10}\nFrench Onion Salad: {count11}\nLobster Bisque: {count12}\nTea: {count13}\nCoffe: {count14}\nCoca: {count15}\nOrange Juice: {count16}')
        if result[0] > 0:
            count1 = count1 - int(self.lineedit.text())
            print(count1)
        if result[0] == 0:
            count1 = count1
            print(count1)
            



    def edit(self):
        if self.lineedit18 != '' or self.lineedit19 != '' or self.lineedit18 != '' or self.lineedit20 != '' or self.lineedit21 != '' or self.lineedit22 != '' or self.lineedit23 != '':
            msg = QMessageBox()
            msg.setText("Succesfull!!")
            msg.exec_()


    def submit(self):
        msg = QMessageBox()
        msg.setText("Thanks for your help!!")
        msg.exec_()

    def search(self):
        count1 = 20
        count2 = 20
        count3 = 20
        count4 = 20
        count5 = 20
        count6 = 20
        count7 = 20
        count8 = 20
        count9 = 20
        count10 = 20
        count11 = 20
        count12 = 20
        count13 = 20
        count14 = 20
        count15 = 20
        count16 = 20
        menu_list = ['Spicy Lobster', 'Baked Scargot', 'Shrimp Cocktail', 'SeaRed Ahi Tuna', 'Filet Mignon, 8ounce', 'Filet Mignon, 12ounce', 'Rib Eye Steak, 18ounce', 'Porter house for two', 'Spinach Salad', 'Caprese Salad', 'French Onion Salad', 'Lobster Bisque', 'Tea', 'Coffe', 'Coca', 'Orange Juice']
        if self.lineedit17.text() == menu_list[0]:
            self.textt.addItem(f'{self.lineedit17.text()}: {count1}')
        elif self.lineedit17.text() == menu_list[1]:
            self.textt.addItem(f'{self.lineedit17.text()}: {count2}')
        elif self.lineedit17.text() == menu_list[2]:
            self.textt.addItem(f'{self.lineedit17.text()}: {count3}')
        elif self.lineedit17.text() == menu_list[3]:
            self.textt.addItem(f'{self.lineedit17.text()}: {count4}')
        elif self.lineedit17.text() == menu_list[4]:
            self.textt.addItem(f'{self.lineedit17.text()}: {count5}')
        elif self.lineedit17.text() == menu_list[5]:
            self.textt.addItem(f'{self.lineedit17.text()}: {count6}')
        elif self.lineedit17.text() == menu_list[6]:
            self.textt.addItem(f'{self.lineedit17.text()}: {count7}')
        elif self.lineedit17.text() == menu_list[7]:
            self.textt.addItem(f'{self.lineedit17.text()}: {count8}')
        elif self.lineedit17.text() == menu_list[8]:
            self.textt.addItem(f'{self.lineedit17.text()}: {count9}')
        elif self.lineedit17.text() == menu_list[9]:
            self.textt.addItem(f'{self.lineedit17.text()}: {count10}')
        elif self.lineedit17.text() == menu_list[10]:
            self.textt.addItem(f'{self.lineedit17.text()}: {count11}')
        elif self.lineedit17.text() == menu_list[11]:
            self.textt.addItem(f'{self.lineedit17.text()}: {count12}')
        elif self.lineedit17.text() == menu_list[12]:
            self.textt.addItem(f'{self.lineedit17.text()}: {count13}')
        elif self.lineedit17.text() == menu_list[13]:
            self.textt.addItem(f'{self.lineedit17.text()}: {count14}')
        elif self.lineedit17.text() == menu_list[14]:
            self.textt.addItem(f'{self.lineedit17.text()}: {count15}')
        elif self.lineedit17.text() == menu_list[15]:
            self.textt.addItem(f'{self.lineedit17.text()}: {count16}')
    
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
        items = []
        quantity = []
        price = []
        date = time.strftime('%d/%m/%Y')
        myFile = open('Receipt.txt', 'w')
        myFile.write(date + '\n')
        myFile.write('ITEMS\t\t\t\tQUANTITY\tPRICE\n')
        myFile.write('----------------------------------------------------------\n')
        self.order_list.addItem(date)
        if result[0] != 0:
            myFile.write(f"Spicy Lobster\t\t{total_list[0]}\t\t{int(result[0])*19}\n")
            self.order_list.addItem(f"Spicy Lobster\t\t{total_list[0]}\t\t{int(result[0])*19}\n")
            
        if result[1] != 0:
            myFile.write(f"Baked Scargot\t\t{total_list[1]}\t\t{int(result[1])*16}\n")
            self.order_list.addItem(f"Baked Scargot\t\t{total_list[1]}\t\t{int(result[1])*16}\n")
        if result[2] != 0:
            myFile.write(f"Shrimp Cocktail\t\t{total_list[2]}\t\t{int(result[2])*16}\n")
            self.order_list.addItem(f"Shrimp Cocktail\t\t{total_list[2]}\t\t{int(result[2])*16}\n")

        if result[3] != 0:
            myFile.write(f"Seared Ahi Tuna\t\t{total_list[3]}\t\t{int(result[3])*17}\n")
            self.order_list.addItem(f"Seared Ahi Tuna\t\t{total_list[3]}\t\t{int(result[3])*17}\n")

        if result[4] != 0:
            myFile.write(f"Filet Mignon, 8ounce\t\t{total_list[4]}\t\t{int(result[4])*36}\n")
            self.order_list.addItem(f"Filet Mignon, 8ounce\t\t{total_list[4]}\t\t{int(result[4])*36}\n")

        if result[5] != 0:
            myFile.write(f"Filet Mignon, 12ounce\t\t{total_list[5]}\t\t{int(result[5])*40}\n")
            self.order_list.addItem(f"Filet Mignon, 12ounce\t\t{total_list[5]}\t\t{int(result[5])*40}\n")

        if result[6] != 0:
            myFile.write(f"Rib Eye Steak, 16ounce\t\t{total_list[6]}\t\t{int(result[6])*39}\n")
            self.order_list.addItem(f"Rib Eye Steak, 16ounce\t\t{total_list[6]}\t\t{int(result[6])*39}\n")

        if result[7] != 0:
            myFile.write(f"Porterhouse For Two\t\t{total_list[7]}\t\t{int(result[7])*40}\n")
            self.order_list.addItem(f"Porterhouse For Two\t\t{total_list[7]}\t\t{int(result[7])*40}\n")

        if result[8] != 0:
            myFile.write(f"Spinach Salad\t\t{total_list[8]}\t\t{float(result[8])*9.5}\n")
            self.order_list.addItem(f"Spinach Salad\t\t{total_list[8]}\t\t{float(result[8])*9.5}\n")

        if result[9] != 0:
            myFile.write(f"Caprese Salad\t\t{total_list[9]}\t\t{float(result[9])*8.5}\n")
            self.order_list.addItem(f"Caprese Salad\t\t{total_list[9]}\t\t{float(result[9])*8.5}\n")

        if result[10] != 0:
            myFile.write(f"French Onion Soup\t\t{total_list[10]}\t\t{int(result[10])*5}\n")
            self.order_list.addItem(f"French Onion Soup\t\t{total_list[10]}\t\t{int(result[10])*5}\n")

        if result[11] != 0:
            myFile.write(f"Lobster Bisque\t\t{total_list[11]}\t\t{int(result[11])*8}\n")
            self.order_list.addItem(f"Lobster Bisque\t\t{total_list[11]}\t\t{int(result[11])*8}\n")

        if result[12] != 0:
            myFile.write(f"Tea\t\t\t\t\t{total_list[12]}\t\t\t\t\t{float(result[12])*2.5}\n")
            self.order_list.addItem(f"Tea\t\t\t\t\t{total_list[12]}\t\t\t\t\t{float(result[12])*2.5}\n")
        
        if result[13] != 0:    
            myFile.write(f"Coffe\t\t\t\t{total_list[13]}\t\t\t\t\t{float(result[13])*3.5}\n")
            self.order_list.addItem(f"Coffe\t\t\t\t{total_list[13]}\t\t\t\t\t{float(result[13])*3.5}\n")

        if result[14] != 0:
            myFile.write(f"Coca\t\t{total_list[14]}\t\t{int(result[14])*2}\n")
            self.order_list.addItem(f"Coca\t\t{total_list[14]}\t\t{int(result[14])*2}\n")

        if result[15] != 0:
            myFile.write(f"Orange Juice\t\t\t{total_list[15]}\t\t\t{int(result[15])*4}\n")
            self.order_list.addItem(f"Orange Juice\t\t\t{total_list[15]}\t\t\t{int(result[15])*4}\n")
        


        myFile.write(f'TOTAL : ${a + b + c + d + e + f + g + h + i + j + k + l + m + n + o + p}')
        myFile.close()


    def order(self):
        paymenttt = Paymnet()
        widget.addWidget(paymenttt)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
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

        self.button.clicked.connect(self.online)
        self.button2.clicked.connect(self.home)

    def online(self):
        onlinepayy = OnlinePay()
        widget.addWidget(onlinepayy)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        

    def home(self):
        msg = QMessageBox()
        msg.setText("You will pay cash on delivery!!")
        msg.setWindowTitle("Payment")
        msg.exec_()


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

app = QApplication(sys.argv)
window  = CustomerProfile()
widget=QtWidgets.QStackedWidget()
widget.addWidget(window)
widget.setFixedWidth(1261)
widget.setFixedHeight(881)
widget.show()
app.exec_()