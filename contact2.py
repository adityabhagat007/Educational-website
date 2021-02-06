#!C:\Users\user\AppData\Local\Programs\Python\Python38\python.exe
print("Content-type:text/html\r\n\r\n")
import mysql.connector
import cgi
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="ardent_pr")
cur=db.cursor()
form=cgi.FieldStorage()
n=form['name'].value
no=form['no'].value
e=form['email'].value
m=form['subject'].value
cur.execute("insert into public values('{0}','{1}','{2}','{3}')".format(n,e,m,no))
db.commit()

print("""
  <link href="//netdna.bootstrapcdn.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
  <script src="//netdna.bootstrapcdn.com/bootstrap/3.0.3/js/bootstrap.min.js"></script>
 <script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
  <!------ Include the above in your HEAD tag ---------->

<!-- http://www.jquery2dotnet.com -->
<div class="container">
    <div class="row">
        <div class="col-sm-6 col-md-6">
            <div class="alert alert-success">
                <button type="button" class="close" data-dismiss="alert" aria-hidden="true">
                    ×</button>
               <span class="glyphicon glyphicon-ok"></span> <strong>Success Message</strong>
                <hr class="message-inner-separator">
                <p>
                   <center> Your MSG successfully sent</center></p>
            </div> """)