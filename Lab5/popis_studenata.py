#!python.exe
import base
import cgi
import os
import session
import db
import password_utils

p=db.get_students()
base.start_html()
for x in p:
    print("<br>" + x[1])
base.end_html()
