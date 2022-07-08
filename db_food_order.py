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
                count integer NOT NULL, 
                date text NOT NULL,
                status text NOT NULL
        )''')


#Combined_input = [(national_code, foods, count, date)]
def insert_table_food(national_code, foods, count, date):
        """insert into food_order table"""
        c.execute(f"INSERT INTO food_order VALUES (?,?,?,?,?)", (national_code, foods, count, date, "Not Confirmed!"))
        conn.commit()


def previous_order(national_code):
        """query to database"""
        c.execute(f"SELECT * FROM food_order WHERE national_code = '{national_code}'")
        conn.commit()
        items = c.fetchall()
        return items

def confriming_order():
        """query to database"""
        c.execute(f"SELECT * FROM food_order WHERE status = 'Not Confirmed!'")
        conn.commit()
        items = c.fetchall()
        return items


def confirmed_order():
        """query to database"""
        c.execute(f"SELECT * FROM food_order WHERE status = 'Confirmed!'")
        conn.commit()
        items = c.fetchall()
        return items


def confirmation():
        """query to database"""
        c.execute(f"UPDATE food_order SET status = 'Confirmed!' WHERE status = 'Not Confirmed!'")
        conn.commit()

