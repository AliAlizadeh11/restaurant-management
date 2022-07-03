import sqlite3

#connect to database
conn = sqlite3.connect('profile_customer.db')

#create a cursor
c = conn.cursor()


def create_table():
        """create a table"""
        c.execute('''CREATE TABLE IF NOT EXISTS customers
                (name text NOT NULL,
                family_name text NOT NULL, 
                phone_number integer NOT NULL, 
                email text NOT NULL, 
                national_code integer NOT NULL, 
                password text NOT NULL, 
                repeat_password text NOT NULL
        )''')


def insert_table():
        """insert into customers table"""
        c.execute('''INSERT INTO customers VALUES (f'')''')
        conn.commit()


def update_table():
        """update records from customers"""
        c.execute("UPDATE customers SET")
        conn.commit()


def delete_table():
        """delete records from customers"""
        c.execute("DELETE FROM customers WHERE")
        conn.commit()


def query():
        """query to database"""
        c.execute('SELECT * FROM customers')
        conn.commit()
        items = c.fetchall()
        for item in items:
                print(item)
                

        #WHERE IN FETCHED VALUES
        c.execute("SELECT * FROM customers WHERE'")
        conn.commit()
        items = c.fetchall()
        for item in items:
                print(item)

        #where with like
        c.execute("SELECT * FROM customers WHERE'")
        conn.commit()
        items = c.fetchall()
        for item in items:
                print(item)


#commit our command
conn.commit()

#close the connection
conn.close()