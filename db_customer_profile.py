import sqlite3

#connect to database
conn = sqlite3.connect('customers.db')

#create a cursor
c = conn.cursor()


def update_table_name():
        """update records from customers"""
        c.execute("UPDATE customers SET name = '' WHERE national_code = ''")
        conn.commit()


def update_table_family_name():
        """update records from customers"""
        c.execute("UPDATE customers SET family_name = '' WHERE national_code = ''")
        conn.commit()


def update_table_phone_number():
        """update records from customers"""
        c.execute("UPDATE customers SET phone_number = '' WHERE national_code = ''")
        conn.commit()


def update_table_email():
        """update records from customers"""
        c.execute("UPDATE customers SET email = '' WHERE national_code = ''")
        conn.commit()


def update_table_password():
        """update records from customers"""
        c.execute("UPDATE customers SET password = '' WHERE national_code = ''")
        conn.commit()


def update_table_photo():
        """update records from customers"""
        c.execute("UPDATE customers SET photo = '' WHERE national_code = ''")
        conn.commit()
        


def query():
        """query to database"""
        c.execute('SELECT * FROM customers')
        conn.commit()
        items = c.fetchall()
                
        #WHERE IN FETCHED VALUES
        c.execute("SELECT * FROM customers WHERE'")
        conn.commit()
        items = c.fetchall()
        
        #where with like
        c.execute("SELECT * FROM customers WHERE'")
        conn.commit()
        items = c.fetchall()


#commit our command
conn.commit()

#close the connection
conn.close()