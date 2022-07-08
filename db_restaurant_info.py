import sqlite3

#connect to database
conn = sqlite3.connect('admin_information.db')

#create a cursor
c = conn.cursor()

def create_table():
        """create a table"""
        c.execute('''CREATE TABLE IF NOT EXISTS admin_information
                (name text NOT NULL, 
                family_name text NOT NULL,
                restaurant_area text NOT NULL,
                restaurant_type text NOT NULL,
                restaurant_menu text NOT NULL,
                restaurant_address text NOT NULL
        )''')

# information = [(name, family_name, restaurant_area, restaurant_type, restaurant_address)]
def insert_table(information):
        """insert into admin_information table"""
        c.execute("INSERT INTO admin_information VALUES (?,?,?,?,?,?)", information)
        conn.commit()


def update_table_name(name):
        """update records from admin_information"""
        c.execute(f"UPDATE admin_information SET name = '{name}'")
        conn.commit()


def update_table_family_name(family_name):
        """update records from admin_information"""
        c.execute(f"UPDATE admin_information SET family_name = '{family_name}'")
        conn.commit()


def update_table_restaurant_area(restaurant_area):
        """update records from admin_information"""
        c.execute(f"UPDATE admin_information SET restaurant_area = '{restaurant_area}'")
        conn.commit()


def update_table_restaurant_type(restaurant_type):
        """update records from admin_information"""
        c.execute(f"UPDATE admin_information SET restaurant_type = '{restaurant_type}'")
        conn.commit()


def update_table_restaurant_menu(restaurant_menu):
        """update records from admin_information"""
        c.execute(f"UPDATE admin_information SET restaurant_menu = '{restaurant_menu}'")
        conn.commit()


def update_table_restaurant_address(restaurant_address):
        """update records from admin_information"""
        c.execute(f"UPDATE admin_information SET restaurant_address = '{restaurant_address}'")
        conn.commit()