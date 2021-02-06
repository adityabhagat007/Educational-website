#!C:\Users\user\AppData\Local\Programs\Python\Python38\python.exe
print("Content-type:text/html\r\n\r\n")
import mysql.connector
import cgi
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="ardent_pr")
cur=db.cursor()
cur.execute("select * from public")
x=cur.fetchall()
db.commit()
print("""
    <html>
    <head>
    <title>view</title>
    <link rel="stylesheet" type="text/css" href="css/table1.css">
    </head>
    <body>
    <h1><u>PUBLIC QUERY</u></h1>
    <table class="content-table" >
    <thead>
    <th>name</th>
    <th>email</th>
    <th>message</th>
    <th>number</th>
    </thead>
    <tbody>
""")
for i in range(len(x)):
    print("""
        <tr  class="active-row">
        <td>{0}</td>
        <td>{1}</td>
        <td>{2}</td>
        <td>{3}</td>
        </tr>
        </tbody>
        """.format(x[i][0],x[i][1],x[i][2],x[i][3]))
print("""
        </table>
        </body>
        </html>
""")