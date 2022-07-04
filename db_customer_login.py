import sqlite3

#connect to database
conn = sqlite3.connect('customers.db')

#create a cursor
c = conn.cursor()


def query(email, password):
        """query to database"""
        c.execute(f"SELECT * FROM customers WHERE email = '{email}'")
        items = c.fetchone()
        
        if items[3] == email and items[5] == password:
            print('login successful')
        else:
            print('login failed')
        

#commit our command
conn.commit()

#close the connection
conn.close()