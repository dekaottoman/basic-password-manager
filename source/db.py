import sqlite3

def create_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS passwords (username TEXT, title TEXT, site_username TEXT, email TEXT, password TEXT)")
    conn.commit()
    conn.close()

def create_user(username:str,password:str):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users VALUES ('%s','%s')" % (username,password))
    conn.commit()
    conn.close()

def get_data():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    conn.close()
    return data

def get_password(username:str):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = '%s'" % username)
    data = cursor.fetchall()
    conn.close()
    return data[0][0]


def delete_user(username:str):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE username = '%s'" % username)
    cursor.execute("DELETE FROM passwords WHERE username = '%s'" % username)
    conn.commit()
    conn.close()

def change_username(username:str, new_username:str):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET username = '%s' WHERE username = '%s'" % (new_username,username))
    conn.commit()
    conn.close()

def change_password(username:str, password:str):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET password = '%s' WHERE username = '%s'" % (password,username))
    conn.commit()
    conn.close()

def create_password(username:str,title:str,site_username:str, email:str,password:str):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO passwords VALUES ('%s','%s','%s','%s','%s')" % (username,title,site_username,email,password))
    conn.commit()
    conn.close()

def get_password_list(username:str):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM passwords WHERE username = '%s'"%username)
    data = cursor.fetchall()
    conn.close()
    return data

def delete_password_from_list(username:str,title:str):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM passwords WHERE username = '%s' AND title = '%s'" % (username, title))
    conn.commit()
    conn.close()