#!C:\Users\user\AppData\Local\Programs\Python\Python38\python.exe
print("Content-type:text/html\r\n\r\n")
import mysql.connector
import cgi
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="ardent_pr")
cur=db.cursor()
form=cgi.FieldStorage()
n=form['name'].value
s=form['stream'].value
e=form['email'].value
a=form['age'].value
c=form['course'].value
num=form['number'].value
u=form['username'].value
p=form['password'].value
cur.execute("insert into student values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(n,s,e,a,c,num,u,p))
db.commit()
print(""" <html>
          <head>
          <title>regestration conformation</title>
          <link rel="stylesheet" type="text/css" href="css/table.css">
          </head>
          <body>
          <h1><center><u>You have sucessfuly enrolled for the course</u></center></h1>
""")