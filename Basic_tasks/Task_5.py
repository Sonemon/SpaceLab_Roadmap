import sqlite3
from fastapi import FastAPI

app = FastAPI(
    title="Task_5"
)
connectionToDB = sqlite3.connect("DBTask5")
cursorDB = connectionToDB.cursor()
 
@app.get("/users")
async def get_all_users():
    query = "SELECT * FROM users;"
    results = await cursorDB.execute(query).fetchall()
    return results
 
@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    return user_id

get_all_users