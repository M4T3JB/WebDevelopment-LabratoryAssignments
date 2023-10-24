#!python.exe
import mysql.connector 
import json

db_conf = {
    "host":"localhost",
    "db_name":"mbvj5",
    "user":"root",
    "passwd":""
}

def get_DB_connection():
    mydb = mysql.connector.connect(
        host=db_conf["host"],
        user=db_conf["user"],
        passwd=db_conf["passwd"],
        database=db_conf["db_name"]
    )
    return mydb

def create_session():
    query = "INSERT INTO sessions (data) VALUES (%s)"
    values = (json.dumps({}),)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()
    return cursor.lastrowid 

def get_session(session_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM sessions WHERE session_id=" + str(session_id))
    myresult = cursor.fetchone()
    return myresult[0], json.loads(myresult[1])

def replace_session(session_id, data):#replace-prvo izbrisi, a onda ubaci (delete/insert)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("""
    REPLACE INTO sessions(session_id,data) 
    VALUES (%s,%s)""",
    (session_id, json.dumps(data)))
    mydb.commit()

def delete_session(session_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM sessions WHERE session_id="+str(session_id))
    
    mydb.commit()
def create_user(name,email,password):
    mydb=get_DB_connection()
    cursor = mydb.cursor()
    query = "INSERT INTO users (data) VALUES (%s %s %s)"
    cursor.execute("""
    INSERT INTO users (ime,email,password) 
    VALUES (%s,%s,%s)""",
    (name, email, password))
    mydb.commit()
    
def get_user(email):
    mydb=get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE email='"+email+"'")
    myresult = cursor.fetchall()
    return myresult

def get_user_by_id(id):
    mydb=get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id="+ str(id))
    myresult = cursor.fetchall()
    return myresult


def check_email(email):
    mydb=get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT email FROM users WHERE email='{email}'")
    myresult = cursor.fetchone()
    return myresult

def check_password(password):
    mydb=get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT password FROM users WHERE password='{password}'")
    myresult = cursor.fetchone()
    return myresult

def change_password(password,email):
    mydb=get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("UPDATE users SET password='"+str(password)+"' WHERE email='"+str(email)+"'")
    mydb.commit()

def populate_subjects(kod,ime,bodovi,godina):
    mydb=get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("""
    INSERT INTO subjects (kod,ime,bodovi,godina) 
    VALUES (%s,%s,%s,%s)""",
    (kod, ime, bodovi,godina))
    mydb.commit()

def get_subjects():
    mydb=get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM subjects")
    myresult = cursor.fetchall()
    return myresult

def get_students():
    mydb=get_DB_connection()
    cursor= mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE uloga = 'student' ")
    myresult= cursor.fetchall()
    return myresult