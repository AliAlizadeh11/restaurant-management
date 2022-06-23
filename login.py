import create_customer
import smtplib
import random


class Login:
    def __init__(self):
        pass

    def forget_password(self):
        recovery_password = random.randint(1001, 10000)
        smtplib_obj = smtplib.SMTP("smtp.gmail.com", 587)
        smtplib_obj.ehlo()
        smtplib_obj.starttls()
        smtplib_obj.login("AP4002Group4@gmail.com", "rginclqnytypwofj")
        smtplib_obj.sendmail("AP4002Group4@gmail.com", f"{create_customer.CreateCustomer.email}", f"Subject:Password recovery\n{recovery_password}")
        smtplib_obj.quit()
        
    def check_validation_email_password(self, email, password):
        global count
        count = 0 
        if Login.email == create_customer.CreateCustomer.email:
            if Login.password == create_customer.CreateCustomer.password:
                pass
            else:
                print("Wrong Password, Please Try again")
                count += 1
                if count == 3:
                    print('Wait thirty seconds please')
                    Login.forget_password()
