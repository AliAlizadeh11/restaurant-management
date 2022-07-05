import sqlite3

#connect to database
conn = sqlite3.connect('shopping_cart.db')

#create a cursor
c = conn.cursor()


def create_table():
        """create a table"""
        c.execute('''CREATE TABLE IF NOT EXISTS shopping_cart
                (national_code integer NOT NULL, 
                foods text NOT NULL, 
                date text NOT NULL
        )''')


#Combined_input = [(national_code, foods, date)]
def insert_table(combined_input):
        """insert into food_order table"""
        c.execute(f"INSERT INTO food_order VALUES (?,?,?)", combined_input)
        conn.commit()



def update_table(national_code, foods):
        """update records from shopping_cart"""
        c.execute(f"UPDATE shopping_cart SET foods = '{foods}' WHERE national_code == '{national_code}'")
        conn.commit()


def delete_table(national_code):
        """delete records from shopping_cart"""
        c.execute(f"DELETE FROM shopping_cart WHERE national_code = '{national_code}'")
        conn.commit()
