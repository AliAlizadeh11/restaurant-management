import sqlite3

#connect to database
conn = sqlite3.connect('admin_login.db')

#create a cursor
c = conn.cursor()


def create_table():
        """create a table"""
        c.execute('''CREATE TABLE IF NOT EXISTS admin_login
                (email text NOT NULL, 
                password text NOT NULL, 
        )''')


def insert_table():
        """insert into admin_login table"""
        information = [('mahdihosseinizade2000@gmail.com', 'mahdi2000')]
        c.execute("INSERT INTO admin_login VALUES (?,?)", information)
        conn.commit()


def check_login_admin(email, password):
        """query to database"""
        c.execute(f"SELECT * FROM admin_login WHERE email = '{email}'")
        items = c.fetchone()
        
        if items == None:
                return False
        
        elif items[0] == email and items[1] == password:
                return True

        else:
                return False