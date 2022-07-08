import sqlite3
from ssl import cert_time_to_seconds

#connect to database
conn = sqlite3.connect('admin_info.db')

#create a cursor
c = conn.cursor()


def create_table():
        """create a table"""
        c.execute('''CREATE TABLE IF NOT EXISTS admin_info
                (email text PRIMARY KEY, 
                password text NOT NULL, 
                name text NOT NULL,
                family_name text NOT NULL,
                restaurant_name text NOT NULL,
                restaurant_area text NOT NULL,
                restauarant_type text NOT NULL,
                restaurant_address text NOT NULL
        )''')


def insert_table():
        """insert into admin_info table"""
        information = ('mahdihosseinizade2000@gmail.com', 'mahdi2000', 'Mahdi', 'Hosseinizad', 'AP4002', '12', 'Coffe Shop', 'iran university of science and technology')
        try:
            c.execute("INSERT INTO admin_info VALUES (?,?,?,?,?,?,?,?)", information)
            conn.commit()
        except Exception as e:
            pass

def check_login_admin(email, password):
        """query to database"""
        c.execute(f"SELECT * FROM admin_info WHERE email = '{email}'")
        items = c.fetchone()
        
        if items == None:
                return False
        
        elif items[0] == email and items[1] == password:
                return True

        else:
                return False

def update_table_name(name):
        """update records from admin_information"""
        c.execute(f"UPDATE admin_info SET name = '{name}'")
        conn.commit()

def update_table_family_name(family_name):
        """update records from admin_information"""
        c.execute(f"UPDATE admin_info SET family_name = '{family_name}'")
        conn.commit()

def update_table_restaurant_name(restaurant_name):
        """update records from admin_information"""
        c.execute(f"UPDATE admin_info SET restaurant_name = '{restaurant_name}'")
        conn.commit()

def update_table_restaurant_area(restaurant_area):
        """update records from admin_information"""
        c.execute(f"UPDATE admin_info SET restaurant_area = '{restaurant_area}'")
        conn.commit()

def update_table_restaurant_type(restaurant_type):
        """update records from admin_information"""
        c.execute(f"UPDATE admin_info SET restaurant_type = '{restaurant_type}'")
        conn.commit()

def update_table_restaurant_address(restaurant_address):
        """update records from admin_information"""
        c.execute(f"UPDATE admin_info SET restaurant_address = '{restaurant_address}'")
        conn.commit()

def info_admin():
    c.execute("SELECT * FROM admin_info WHERE email = 'mahdihosseinizade2000@gmail.com'")
    items = c.fetchone()
    return items

