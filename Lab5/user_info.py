#!python.exe
import base
import cgi
import os
import session
import db
import password_utils

params = cgi.FieldStorage()
if params:
    if db.check_password(params.getvalue('email')):
        user = db.get_user(params.getvalue('email'))
        if params.getvalue('password') == params.getvalue('repeat_password') and password_utils.verify_password(params.getvalue('old_password'),user[0][3]):
            db.change_password(password_utils.hash_password(params.getvalue('password')),params.getvalue('email'))
            print("location: ./login.py")

print("""
    <!DOCTYPE html>
    <html>
    <head><a href="./index.py">Index</a><a href="./logout.py">Logout</a></head>
    <body>
    <form action="">
    <label>Email:</label><br>
    <input type="email" name="email" value=""><br>
    <label>Old password:</label><br>
    <input type="password" name="old_password" value=""><br>
    <label>Password:</label><br>
    <input type="password" name="password" value=""><br>
    <label>Repeat password:</label><br>
    <input type="password" name="repeat_password" value=""><br><br>
    <input type="submit" value="Submit">
    </form> """)
     
print("""</body>
    </html>
    """)
