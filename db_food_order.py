import sqlite3

#connect to database
conn = sqlite3.connect('food_order.db')

#create a cursor
c = conn.cursor()


def create_table():
        """create a table"""
        c.execute('''CREATE TABLE IF NOT EXISTS food_order
                (national_code integer NOT NULL, 
                foods text NOT NULL, 
                date text NOT NULL
        )''')


#Combined_input = [(national_code, foods, date)]
def insert_table(combined_input):
        """insert into food_order table"""
        c.execute(f"INSERT INTO food_order VALUES (?,?,?)", combined_input)
        conn.commit()
