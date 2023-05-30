import sqlite3
from os.path import exists
from werkzeug.security import generate_password_hash

def fileExists():
    user_data_name = str(input("Enter the database name:"))

    database_exists = exists("C:/Users/admin/Desktop/web app with python/instance/"+user_data_name)


    if(database_exists):
        print("File already exists:")
    else:
        table_creator(user_data_name)

def table_creator(file_name):
    conn = sqlite3.connect("C:/Users/admin/Desktop/web app with python/instance/"+file_name)
    cur = conn.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY ASC, email STRING, password STRING, first_name STRING, permission SRING)")
    cur.execute(f"INSERT INTO user (email, password, first_name, permission) VALUES (?,?,?,?)",("admin@gmail.com",generate_password_hash('admin123', method='sha256'),"admin","0,"))
    conn.commit()
    conn.close()
fileExists()

