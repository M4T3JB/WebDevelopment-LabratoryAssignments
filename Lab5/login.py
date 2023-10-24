#!python.exe
import base
import cgi
import os
import session
import db
import password_utils

params = cgi.FieldStorage()
if params and db.get_user(params.getvalue('email')):
    user = db.get_user(params.getvalue('email'))
    if password_utils.verify_password( params.getvalue('password'),user[0][3]):
        session.get_or_create_session_id_user(user[0][0])
        print("location: ./index.py")
    else:
        print("location: ./login.py")

print("""
    <!DOCTYPE html>
    <html>
    <head><a href="./registration.py">Register</a></head>
    <body>
    <form action="">
    <label>Email:</label><br>
    <input type="email" name="email" value=""><br>
    <label>Password:</label><br>
    <input type="password" name="password" value=""><br>
    <input type="submit" value="Submit">
    </form> """)
if params:
    print("Greska pri loginu")
     
print("""</body>
    </html>
    """)
