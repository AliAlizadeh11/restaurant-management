import create_customer
import random
import smtplib


def discount_code(customer_email):
    code_part1 = random.choice(['uta', 'utb', 'utc', 'ute', 'utf']) 
    code_part2 = random.randint(1000, 100000)
    final_code = str(code_part1) + str(code_part2)
    
    smtplib_obj = smtplib.SMTP("smtp.gmail.com", 587)
    smtplib_obj.ehlo()
    smtplib_obj.starttls()
    
    smtplib_obj.login("AP4002Group4@gmail.com", "rginclqnytypwofj")
    smtplib_obj.sendmail("AP4002Group4@gmail.com", f"{create_customer.CreateCustomer.email}", f"Subject:discount code\n{final_code}")
    smtplib_obj.quit()