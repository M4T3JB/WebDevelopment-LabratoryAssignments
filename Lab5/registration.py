#!python.exe
import base
import cgi
import os
import session
import db
import password_utils

params = cgi.FieldStorage()
if params:
    email_fetched = db.check_email(params.getvalue('email'))
    if params.getvalue('password')==params.getvalue('repeat_password') and not email_fetched == params.getvalue('email'):
        hashed_pass=password_utils.hash_password(params.getvalue('password'))
        db.create_user(params.getvalue('name'),params.getvalue('email'),hashed_pass)
        print("location: ./login.py")

print("""
    <!DOCTYPE html>
    <html>
    <head><a href="./login.py">Login</a></head>
    <body>
    <form action="">
    <label>Name:</label><br>
    <input type="text" name="name" value=""><br>
    <label>Email:</label><br>
    <input type="email" name="email" value=""><br>
    <label>Password:</label><br>
    <input type="password" name="password" value=""><br>
    <label>Repeat password:</label><br>
    <input type="password" name="repeat_password" value=""><br><br>
    <input type="submit" value="Submit">
    </form> """)
if params:
    print("Lozinke se ne poklapaju ili je email zauzet")     
print("""</body>
    </html>
    """)

