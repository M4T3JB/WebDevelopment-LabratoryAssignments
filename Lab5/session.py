#!python.exe
import db
import os
from http import cookies

def get_or_create_session_id():
    http_cookies_str = os.environ.get('HTTP_COOKIE', '')
    get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)
    session_id = get_all_cookies_object.get("session_id").value if get_all_cookies_object.get("session_id") else None
    if session_id is None:
        session_id = db.create_session()
        cookies_object = cookies.SimpleCookie()
        cookies_object["session_id"] = session_id
        print (cookies_object.output()) #upisivanje cookie-a u header
    return session_id

def get_or_create_session_id_user(user_id):
    http_cookies_str = os.environ.get('HTTP_COOKIE', '')
    get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)
    session_id = get_all_cookies_object.get("session_id").value if get_all_cookies_object.get("session_id") else None
    if session_id is None:
        session_id = db.create_session()
        cookies_object = cookies.SimpleCookie()
        cookies_object["session_id"] = session_id
        cookies_object["user_id"] = user_id
        print (cookies_object.output()) #upisivanje cookie-a u header
    return session_id

def add_to_session(params):
    session_id = get_or_create_session_id()
    _, data = db.get_session(session_id)#vracanje do sada odabranih podataka
    for status in params.keys():
        data[status] = params[status].value
    db.replace_session(session_id, data)

def get_all_from_session(session_id):
    data = db.get_session(session_id)
    return data


