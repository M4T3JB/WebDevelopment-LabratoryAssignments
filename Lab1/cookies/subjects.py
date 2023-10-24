#!python.exe
from http import cookies
import os

subjects = {
    'ip' : { 'name' : 'Introduction to programming' , 'year' : 1, 'ects' : 6 },
    'c1' : { 'name' : 'Calculus 1' , 'year' : 1, 'ects' : 7 },
    'cu' : { 'name' : 'Computer usage' , 'year' : 1, 'ects' : 5 },
    'dmt' : { 'name' : 'Digital and microprocessor technology', 'year' : 1, 'ects' : 6 },
    'db' : { 'name' : 'Databases' , 'year' : 2, 'ects' : 6 },
    'c2' : { 'name' : 'Calculus 2' , 'year' : 2, 'ects' : 7 },
    'dsa' : { 'name' : 'Data structures and alghoritms' , 'year' : 2, 'ects' : 5 },
    'ca' : { 'name' : 'Computer architecture', 'year' : 2, 'ects' : 6 },
    'isd' : { 'name' : 'Information systems design' , 'year' : 3, 'ects' : 5 },
    'c3' : { 'name' : 'Calculus 3' , 'year' : 3, 'ects' : 7 },
    'sa' : { 'name' : 'Server Architecture' , 'year' : 3, 'ects' : 6 },
    'cds' : { 'name' : 'Computer and data security', 'year' : 3, 'ects' : 6 }
};
        
year_names = {
        1 : '1st Year',
        2 : '2nd Year',
        3 : '3rd Year'
};

year_ids = {
        '1st Year' : 1,
        '2nd Year' : 2,
        '3rd Year' : 3
};

status_names = {
    'not' : 'Not selected',
    'enr' : 'Enrolled',
    'pass' : 'Passed',
};

def make_cookies(params):
    for key in subjects:
        if params.getvalue(key):
            cookie = cookies.SimpleCookie()
            cookie[key] = params.getvalue(key)
            print(cookie.output())

def get_cookies(cookies):
    dictionary = {}
    for key in subjects:
        if cookies.get(key):
         dictionary[key] = cookies.get(key).value
    return dictionary

def display_year():
    for key in year_names:
        print ('<input type="submit" name="button" value="''' + year_names[key] + '">')
    print ('<input type="submit" name="button" value="Upisni List">')


def display_subject(subject, id, dicti): 
    print('<br>')
    print('<tr>')
    print ('<td>' + subject + '</td><td>')
    for key in status_names:
        if(id in dicti and key == dicti[id]) :
            print('''<input type="radio" name="''' + id +'''" value="''' + key + '''" checked="checked">
                '''+ status_names[key]+'''
            ''')
        else:
            print('''<input type="radio" name="''' + id +'''" value="''' + key + '''">
                    '''+ status_names[key]+'''
            ''')
    print('</td></tr>')
            
def display_subject_on_year(year, dicti):
    print('<table>')
    if(year == "Upisni List"):
        ukupni = 0
        print('<td> Predmet </td><td> Status </td><td> Bodovi </td>')
        for key in subjects:
            if(key in dicti):
                print('<tr>')
                ukupni += int(subjects[key]['ects'])
                print('<td>',subjects[key]['name'],'</td>', '<td>',status_names[dicti[key]],'</td>', '<td>',subjects[key]['ects'], '</td>')
                print('</tr>')
        print('<tr><td></td><td> Ukupno </td><td>', ukupni, '</td></tr>')

    else:
        print('''<tr><td>'''+ str(year) +'''st Year</td><td>Status</td></tr>''')
        for subject in subjects:
            if(subjects[subject]['year'] == year):
                display_subject(subjects[subject]['name'], subject, dicti)
    print('</table>')