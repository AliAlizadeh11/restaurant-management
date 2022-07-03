import sqlite3

#connect to database
conn = sqlite3.connect('customer.db')

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
        c.execute('''INSERT INTO customers VALUES
                ('ali','alizadeh',09140973808,'alicsprogrammer@gmail.com',3044775588,'Ali007','Ali007')''')


def update_table():
        """update records from customer"""
        c.execute("UPDATE customers SET family_name = 'alizadeh' WHERE name = 'fatemeh'")
        conn.commit()


def delete_table():
        """delete records from customers"""
        c.execute("DELETE FROM customers WHERE national_code = 340518781")
        conn.commit()



def query_table():
        """query to database"""
        c.execute('SELECT * FROM customers')
        items = c.fetchall()
        for item in items:
                print(item)

        #WHERE IN FETCHED VALUES
        # c.execute("SELECT * FROM customers WHERE national_code = '3040718161'")
        # items = c.fetchall()
        # for item in items:
        #         print(item)

        #where with like
        # c.execute("SELECT * FROM customers WHERE family_name LIKE 'al%'")
        # items = c.fetchall()
        # for item in items:
        #         print(item)


#commit our command
conn.commit()

#close the connection
conn.close()
