import sqlite3

#connect to database
conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()


def extract_national_code(email_or_national_code):
    '''query to database for extracting customer's information'''
    c.execute(f"SELECT * FROM customers WHERE email = '{email_or_national_code}' or national_code = '{email_or_national_code}'")
    items = c.fetchone()
    return items


def query_login(email, password):
        """query to database"""
        c.execute(f"SELECT * FROM customers WHERE email = '{email}'")
        items = c.fetchone()
        
        if items == None:
            return False
        
        elif items[3] == email and items[5] == password:
            return True
            
        else:
            return False