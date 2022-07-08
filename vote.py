import sqlite3

#connect to database
conn = sqlite3.connect('vote.db')

#create a cursor
c = conn.cursor()

def create_table():
        """create a table"""
        c.execute('''CREATE TABLE IF NOT EXISTS vote
                (content text NOT NULL)''')

create_table()

def insert_table_vote(content):
        try:
                """insert into vote table"""
                c.execute(f"INSERT INTO vote VALUES ('{content}')")
                conn.commit()
        except Exception as e:
                print(e)


def votes():
        c.execute(f"SELECT * FROM vote")
        items = c.fetchall()
        return items[0][0]



