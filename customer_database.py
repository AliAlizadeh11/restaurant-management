import sqlite3

#connect to database
conn = sqlite3.connect('customer.db')

#connect to database in RAM
# conn = sqlite3.connect(':memory:')

#create a cursor
c = conn.cursor()

#create a table
c.execute('''CREATE TABLE IF NOT EXISTS customers
        (name text NOT NULL,
        family_name text NOT NULL, 
        phone_number integer NOT NULL, 
        email text NOT NULL, 
        national_code integer NOT NULL, 
        password text NOT NULL, 
        repeat_password text NOT NULL
)''')

#1
#insert into customers table
c.execute('''INSERT INTO customers VALUES
        ('ali','alizadeh',09140973808,'alicsprogrammer@gmail.com',3044775588,'Ali007','Ali007')''')

# 2
#insert many records into customers table
many_customers = [
                ('koosha','lahouti',9120973808,'kooshacsprogrammer@gmail.com',3040718161,'Kousha007','Kousha007')
                ]

c.executemany("INSERT INTO customers VALUES(?,?,?,?,?,?,?)", many_customers)
conn.commit()


#query to database
c.execute('SELECT * FROM customers')
print(c.fetchone())
print(c.fetchone()[2])
print(c.fetchmany(2))
items = c.fetchall()
for item in items:
        print(item[0])

#WHERE IN FETCHED VALUES
c.execute("SELECT * FROM customers WHERE national_code = '3040718161'")
items = c.fetchall()
for item in items:
        print(item)

#where with like
c.execute("SELECT * FROM customers WHERE family_name LIKE 'al%'")
items = c.fetchall()
for item in items:
        print(item)
        

#update records from customer
c.execute("UPDATE customers SET family_name = 'alizadeh' WHERE name = 'fatemeh'")
conn.commit()

        
# delete records from customers
c.execute("DELETE FROM customers WHERE national_code = 340518781")
conn.commit()


items = c.fetchall()
for item in items:
        print(item)
        
#commit our command
conn.commit()

#close the connection
conn.close()
