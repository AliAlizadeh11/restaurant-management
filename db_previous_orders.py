import sqlite3

#connect to database
conn = sqlite3.connect('food_order.db')

#create a cursor
c = conn.cursor()


def previous_order(national_code):
        """query to database"""
        c.execute(f"SELECT * FROM customers WHERE national_code = '{national_code}'")
        conn.commit()
        items = c.fetchall()
        return items
