#!python.exe
import base
import cgi
from http import cookies
import db
import password_utils
subjects = {
    'ip' : { 'name' : 'Introduction to programming' , 'year' : '1st Year', 'ects' : 6 },
    'c1' : { 'name' : 'Calculus 1' , 'year' : '1st Year', 'ects' : 7 },
    'cu' : { 'name' : 'Computer usage' , 'year' : '1st Year', 'ects' : 5 },
    'dmt' : { 'name' : 'Digital and microprocessor technology', 'year' : '1st Year', 'ects' : 6 },
    'db' : { 'name' : 'Databases' , 'year' : '2nd Year', 'ects' : 6 },
    'c2' : { 'name' : 'Calculus 2' , 'year' : '2nd Year', 'ects' : 7 },
    'dsa' : { 'name' : 'Data structures and alghoritms' , 'year' : '2nd Year', 'ects' : 5 },
    'ca' : { 'name' : 'Computer architecture', 'year' : '2nd Year', 'ects' : 6 },
    'isd' : { 'name' : 'Information systems design' , 'year' : '3rd Year', 'ects' : 5 },
    'c3' : { 'name' : 'Calculus 3' , 'year' : '3rd Year', 'ects' : 7 },
    'sa' : { 'name' : 'Server Architecture' , 'year' : '3rd Year', 'ects' : 6 },
    'cds' : { 'name' : 'Computer and data security', 'year' : '3rd Year', 'ects' : 6 }
    }

