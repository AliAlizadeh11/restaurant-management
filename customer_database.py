import sqlite3

#connect to database
conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()


def create_table():
        """create a table"""
        c.execute('''CREATE TABLE IF NOT EXISTS customer
                (name text NOT NULL,
                family_name text NOT NULL, 
                phone_number integer NOT NULL, 
                email text NOT NULL, 
                national_code integer NOT NULL,
                address text NOT NULL,
                password text NOT NULL, 
                repeat_password text NOT NULL
        )''')


def insert_table(customer_input):
        """insert into customer table"""
        c.execute("INSERT INTO customer VALUES (?,?,?,?,?,?,?,?)", customer_input)
        conn.commit()