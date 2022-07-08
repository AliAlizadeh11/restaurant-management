import sqlite3

#connect to database
conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()


def query(email, password):
        """query to database"""
        c.execute(f"SELECT * FROM customers WHERE email = '{email}'")
        items = c.fetchone()
        if items == None:
            return "not exist"
        if items[3] == email and items[5] == password:
            return True
        else:
            return False