import sqlite3

#connect to database
conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()


def update_table_name(name, national_code):
        """update records from customers"""
        c.execute(f"UPDATE customers SET name = '{name}' WHERE national_code = '{national_code}'")
        conn.commit()


def update_table_family_name(family_name, national_code):
        """update records from customers"""
        c.execute(f"UPDATE customers SET family_name = '{family_name}' WHERE national_code = '{national_code}'")
        conn.commit()


def update_table_phone_number(phone_number, national_code):
        """update records from customers"""
        c.execute(f"UPDATE customers SET phone_number = '{phone_number}' WHERE national_code = '{national_code}'")
        conn.commit()


def update_table_email(email, national_code):
        """update records from customers"""
        c.execute(f"UPDATE customers SET email = '{email}' WHERE national_code = '{national_code}'")
        conn.commit()


def update_table_password(password, national_code):
        """update records from customers"""
        c.execute(f"UPDATE customers SET password = '{password}' WHERE national_code = '{national_code}'")
        conn.commit()


def update_table_photo(photo, national_code):
        """update records from customers"""
        c.execute(f"UPDATE customers SET photo = '{photo}' WHERE national_code = '{national_code}'")
        conn.commit()
