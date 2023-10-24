#!python.exe
import base
import cgi
import os
import session
import db
from http import cookies

c =cookies.SimpleCookie(os.environ.get('HTTP_COOKIE'))
db.delete_session(c.get("session_id").value)
for k in c:
    c[k]['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'

print("location: ./login.py")

http_cookies_str = os.environ.get('HTTP_COOKIE', '')
get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)
s_id=c.get("session_id").value
db.delete_session(s_id)
for k in get_all_cookies_object:
    get_all_cookies_object[k]['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'
print(get_all_cookies_object)
print("location: ./login.py")

print("""
    <!DOCTYPE html>
    <html>
    <head></head>
    <body>
    </body>
    </html>
    """)