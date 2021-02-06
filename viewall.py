#!C:\Users\user\AppData\Local\Programs\Python\Python38\python.exe
print("Content-type:text/html\r\n\r\n")
import mysql.connector
import cgi
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="ardent_pr")
cur=db.cursor()
cur.execute("select * from student")
x=cur.fetchall()
db.commit()
print("""
    <html>
    <head>
    <title>view</title>
    <link rel="stylesheet" type="text/css" href="css/table1.css">
    </head>
    <body>
    <h1><u>ENROLLED STUDENTS</u></h1>
    <table class="content-table" >
    <thead>
    <th>name</th>
    <th>stream</th>
    <th>email</th>
    <th>age</th>
    <th>course</th>
    <th>number</th>
    <th>username</th>
    <th>password</th>
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
        <td>{4}</td>
        <td>{5}</td>
        <td>{6}</td>
        <td>{7}</td>
        </tr>
        </tbody>
        """.format(x[i][0],x[i][1],x[i][2],x[i][3],x[i][4],x[i][5],x[i][6],x[i][7]))
print("""
        </table>
        </body>
        </html>
""")
    

