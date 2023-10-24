#!python.exe

def start_html():
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
    <form action='index.py' method='post'>
     """)

def end_html():
    print("""
    </form>
    </body>
    </html>
    """)