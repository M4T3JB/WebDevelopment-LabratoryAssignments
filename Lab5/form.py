import base
import cgi
import os
from http import cookies
import session
import json
import db

s=db.get_subjects()
subjects=dict()
for x in s:
    subjects[x[1]]={'name':x[2],'ects':x[3],'year':x[4]}
        
year_names = {
        1 : '1st Year',
        2 : '2nd Year',
        3 : '3rd Year'
    }

year_ids = {
        '1st Year' : 1,
        '2nd Year' : 2,
        '3rd Year' : 3
}

status_names = {
    'not' : 'Not selected',
    'enr' : 'Enrolled',
    'pass' : 'Passed',
}
    


def display_form(year,params):
    checkedU=""
    checkedN=""
    checkedP=""
    print('<form action="./index.py" method="post">')
    print('<input type="submit" name="form_num" value="1st Year">')
    print('<input type="submit" name="form_num" value="2nd Year">')
    print('<input type="submit" name="form_num" value="3rd Year">')
    print('<input type="submit" name="form_num" value="Enrollment">')
    print('<br>')
    print('<table>')
    if year == "Enrollment":
        sess_id = session.get_or_create_session_id()
        data = db.get_session(sess_id)
        for k in data[1]:
            if not k=="form_num":
                print(subjects[k]['name']+'    '+ data[1][k]+'<br>')
    else:
        sess_id = session.get_or_create_session_id()
        data = db.get_session(sess_id)
        for key in subjects:
            if subjects[key]['year'] == year_ids[year]:
                if os.environ.get('HTTP_COOKIE'):
                    if key in data[1] and data[1][key]=="Upisuje":
                        checkedU="checked"
                    else:
                        checkedU=""
                    if key in data[1] and data[1][key]=="Ne upisuje":
                        checkedN="checked"
                    else:
                        checkedN=""
                    if key in data[1] and data[1][key]=="Polozio":
                        checkedP="checked"
                    else:
                        checkedP=""
                print ('<tr>' + subjects[key]['name'] + '</tr>' + ': <input type="radio" name="' + key + '" value="Upisuje"'+ checkedU + '> Upisuje')
                print ('<input type="radio" name="' + key + '" value="Ne upisuje"'+ checkedN + '> Ne upisuje')
                print ('<input type="radio" name="' + key + '" value="Polozio"'+ checkedP + '> Polozio<br>')
    print('</table>')
    print('</form>')
    
