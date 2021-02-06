#!C:\Users\user\AppData\Local\Programs\Python\Python38\python.exe
print("Content-type:text/html\r\n\r\n")
import mysql.connector
import cgi
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="ardent_pr")
cur=db.cursor()
form=cgi.FieldStorage()
n=form['name'].value
#s=form['stream'].value
e=form['email'].value
#a=form['age'].value
c=form['course'].value
num=form['number'].value
u=form['username'].value
#p=form['password'].value
#cur.execute("update student set name='{0}',email='{1}',number='{2}',course='{3}' where username='{4}' ".format(n,e,num,c,u)) 
#db.commit()
print("""  <html>
            <head>
            <title>home</title>
            <link rel="stylesheet" type="text/css" href="css/tablemakover.css">
            </head>
            <body>
            <h1><center><u>UPDATE YOUR DETAILS</u></center></h1>
            <form action="update_final.py" method="get">
                <table class="content-table">
                <tr class="active-row">
                <td>name</td>
                <td><input type="text" name="name" value="{0}"></td>
                </tr>
                 <tr class="active-row">
                <td>email</td>
                <td><input type="text" name="email" value="{1}"></td>
                </tr>
                 <tr class="active-row">
                <td>course</td>
                <td><input type="text" name="course" value="{2}"></td>
                </tr>
                 <tr class="active-row">
                <td>number</td>
                <td><input type="text" name="number" value="{3}"></td>
                </tr>
                <tr class="active-row">
                <td>username</td>
                <td><input type="hidden" name="username" value='{4}'></td>
                </tr>
                <tr class="active-row">
                <td><input type="submit"></td>
                </tr>
                </table>
                </form>
            </body>
            </html>
           """.format(n,e,c,num,u))
     
            