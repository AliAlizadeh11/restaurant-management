import sqlite3
from tkinter import E
def dict_factory(cursor, row):
    dictionary = {}
    for index, column in enumerate(cursor.description):
        dictionary[column[0]] = row[index]
    return dictionary

#connect to database
conn = sqlite3.connect('admin_menu.db')
conn.row_factory = dict_factory
#create a cursor
c = conn.cursor()

def create_table():
        """create a table"""
        c.execute('''CREATE TABLE IF NOT EXISTS admin_menu
                (name text NOT NULL,
                count integer NOT NULL,
                price  integer NOT NULL,
                date text NOT NULL
        )''')

create_table()
def insert_table_food_new(name , count , date, price):
        try:
                """insert into admin_menu table"""
                c.execute("INSERT INTO admin_menu VALUES (?,?,?,?)", (name, count, price, date))
                conn.commit()
        except Exception as e:
                print(e)
        


def update_price_table_food(name, count, date, price):
        """update records from admin_menu"""
        c.execute(f"UPDATE admin_menu SET price = '{price}' WHERE name = '{name}' AND date = '{date}'")
        conn.commit()

def increase(name, count, date):
        c.execute(f"SELECT * FROM admin_menu  WHERE name = '{name}' AND date = '{date}'")
        item = c.fetchone()
        c.execute(f"UPDATE admin_menu SET count = \'{item['count'] + count}\' WHERE name = '{name}' AND date = '{date}'")
        conn.commit()

def decrease(name, count, date):
        c.execute(f"SELECT * FROM admin_menu  WHERE name = '{name}' AND date = '{date}'")
        item = c.fetchone()
        c.execute(f"UPDATE admin_menu SET count = \'{item['count'] - count}\' WHERE name = '{name}' AND date = '{date}'")
        conn.commit()


def inventory(date):
        c.execute(f"SELECT * FROM admin_menu WHERE date = '{date}'")
        items = c.fetchall()
        return items


#print(inventory("2022-07-08"))
#increase('Spicy Lobster', 10, "2022-07-08")