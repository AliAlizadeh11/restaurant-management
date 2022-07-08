import sqlite3

#connect to database
conn = sqlite3.connect('admin_menu.db')

#create a cursor
c = conn.cursor()

def create_table():
        """create a table"""
        c.execute('''CREATE TABLE IF NOT EXISTS admin_menu
                (name text NOT NULL,
                count integer NOT NULL, 
        )''')


def insert_table(admin_menu_input):
        """insert into admin_menu table"""
        c.execute("INSERT INTO admin_menu VALUES (?,?)", admin_menu_input)
        conn.commit()
        
admin_menu_input = [('spicy Lobster', 20),('Baked Escargot', 20),('Shrimp Cocktail', 20),('Seared Ahi Tuna', 20),('Filet Mignon 8 ounce', 20),('Rib Eye Steak, 18 ounce', 20),('Porterhouse for two', 20),('Filet Mignon 12 ounce', 20),('French Onion Soup', 20),('Lobster Bisque', 20),('Caprese Salad', 20),('Spinach Salad', 20),('Coca', 20),('Tea', 20),('Coffee', 20),('Orange Juice', 20)]


def update_table_food(name, count):
        """update records from admin_menu"""
        c.execute(f"UPDATE admin_menu SET count = '{count}' WHERE name = '{name}'")
        conn.commit()

def delete_table_food(name):
        "delete records from admin_menu"
        c.execute(f"DELETE FROM admin_menu WHERE name = '{name}'")
