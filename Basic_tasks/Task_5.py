import sqlite3
from fastapi import FastAPI

app = FastAPI()
connectionToDB = sqlite3.connect("DBTask5")
cursorDB = connectionToDB.cursor()

# создаем таблицу users
cursorDB.execute("""CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                    name TEXT, 
                    nickname TEXT, 
                    age INTEGER)
                """)

# создаем таблицу posts
cursorDB.execute("""CREATE TABLE IF NOT EXISTS posts
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                    uid INTEGER,  
                    title TEXT)
                """)

connectionToDB.commit()
