from fastapi import FastAPI, Body
import uvicorn
import sqlite3

app = FastAPI()
conn = sqlite3.connect('db.sqlite')


@app.on_event('startup')
def create_db():
    cursor = conn.cursor()
    cursor.execute('''
        create table if not exists users(
            id integer primary key,
            username varchar not null,
            password varchar not null
        );
    ''')
    cursor.close()


@app.get('/')
def index():
    return 'Hello, World!'


@app.post('/login')
def login(username: str = Body(...), password: str = Body(...)):
    cursor = conn.cursor()
    cursor.execute('''
        select * from users where username=? and password=?
    ''', (username, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user


@app.post('/test')
def test():
    cursor = conn.cursor()
    cursor.execute('''
        insert into users(username, password) values ('test', 'password')''')
    conn.commit()
    cursor.close()
    conn.close()


uvicorn.run(app)
