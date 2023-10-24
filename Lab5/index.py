#!python.exe
import base
import cgi
import os
import form
from http import cookies
import session
import db

params = cgi.FieldStorage()
http_cookies_str = os.environ.get('HTTP_COOKIE', '')
get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)
if not get_all_cookies_object.get("user_id"):
    print("location: ./login.py")
else:
    user = db.get_user_by_id(get_all_cookies_object.get("user_id").value)
fm = params.getvalue('form_num')
if not fm:
    fm='1st Year'

if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    session.add_to_session(params) 



print ('Content-Type: text/html\n')


base.start_html()
print('<br><br>')
print("Welcome "+user[0][1])
form.display_form(fm,params)
print('<br><br>')
base.end_html()





