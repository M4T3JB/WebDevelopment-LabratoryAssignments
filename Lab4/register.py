#!python.exe

import base
import password_utils
import session



print("""
 <!DOCTYPE html>
    <html>
    <head>
    <style>
    table, th, td {
    border:1px solid black;
    }
    </style>
    </head>
    <body>
    <form action='login.py' method='post'>

<label for="name">Name:</label>
		<input type="text" name="name" id="name" required><br><br>
		<label for="email">Email:</label>
		<input type="email" name="email" id="email" required><br><br>
		<label for="password">Password:</label>
		<input type="password" name="password" id="password" required><br><br>
		<label for="password2">Repeat Password:</label>
		<input type="password" name="password2" id="password2" required><br><br>
		<input type="submit" value="Register">
</form>
    </body>
    </html>
""")
