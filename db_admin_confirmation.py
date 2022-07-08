import sqlite3

#connect to database
conn = sqlite3.connect('admin_confirmation.db')

#create a cursor
c = conn.cursor()


def create_table():
        """create a table"""
        c.execute('''CREATE TABLE IF NOT EXISTS admin_confirmation
                (foods text NOT NULL
        )''')

#information = [food1, food2, food3, ...] ----> list must be without tuple
def insert_table(information):
        """insert into admin_confirmation table"""
        c.execute("INSERT INTO admin_confirmation VALUES (?)", information)
        conn.commit()
