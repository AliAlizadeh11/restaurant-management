import sqlite3

#connect to database

class Profile:
        def __init__(self, national_code):
                self.national_code = national_code
                self.conn = sqlite3.connect('customer.db')
                self.c = self.conn.cursor()   

        def update_table_name(self, name):
                """update records from customers"""
                self.c.execute(f"UPDATE customers SET name = '{name}' WHERE national_code = '{self.national_code}'")
                self.conn.commit()


        def update_table_family_name(self, family_name):
                """update records from customers"""
                self.c.execute(f"UPDATE customers SET family_name = '{family_name}' WHERE national_code = '{self.national_code}'")
                self.conn.commit()


        def update_table_phone_number(self, phone_number):
                """update records from customers"""
                self.c.execute(f"UPDATE customers SET phone_number = '{phone_number}' WHERE national_code = '{self.national_code}'")
                self.conn.commit()


        def update_table_email(self, email):
                """update records from customers"""
                self.c.execute(f"UPDATE customers SET email = '{email}' WHERE national_code = '{self.national_code}'")
                self.conn.commit()


        def update_table_password(self, password):
                """update records from customers"""
                self.c.execute(f"UPDATE customers SET password = '{password}' WHERE national_code = '{self.national_code}'")
                self.conn.commit()
        
        def update_table_repeat_pass(self, repeat_pass):
                """update records from customers"""
                self.c.execute(f"UPDATE customers SET repeat_password = '{repeat_pass}' WHERE national_code = '{self.national_code}'")
                self.conn.commit()


        def update_table_photo(self, photo):
                """update records from customers"""
                self.c.execute(f"UPDATE customers SET photo = '{photo}' WHERE national_code = '{self.national_code}'")
                self.conn.commit()