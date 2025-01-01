import sqlite3

class Database:
    def __init__(self):
        self.conn = self.initiateConnection()

    def initiateConnection(self):
        conn = sqlite3.connect('movie_tracker.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY,
                title TEXT,
                year INTEGER,
                description TEXT,
                status TEXT,
                progress INTEGER
              )''')
        conn.commit()
        conn.close()
        return conn

    def getConnection(self):
        self.conn = sqlite3.connect('movie_tracker.db')
        return self.conn
    
