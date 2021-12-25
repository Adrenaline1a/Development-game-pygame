import sqlite3


class Log():
    def __init__(self):
        self.conn = sqlite3.connect("Game_BD.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                           login  TEXT,
                           password TEXT 
                            )""")
        self.conn.commit()
        self.user_login = input('Login: ')
        self.user_pass = input('Password: ')
        self.cursor.execute("SELECT login FROM users")
        if self.cursor.fetchone() is None:
            self.cursor.execute(f"INSERT INTO users VALUES (?, ?)", (self.user_login, self.user_pass))
            self.conn.commit()
        else:
            print("Такая запись уже есть")
