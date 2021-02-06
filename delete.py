#!C:\Users\user\AppData\Local\Programs\Python\Python38\python.exe
print("Content-type:text/html\r\n\r\n")
import mysql.connector
import cgi
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="ardent_pr")
cur=db.cursor()
form=cgi.FieldStorage()
n=form['name'].value
u=form['username'].value
#e=form['email'].value
#c=form['course'].value
#um=form['number'].value
cur.execute("delete from student where username='{0}'".format(u))
db.commit()
print("""<link href="//netdna.bootstrapcdn.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
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
                   <center> You successfully delete the account</center></p>
            </div>
        </div>
         </div>
        <div class="col-sm-6 col-md-6">
            <div class="alert alert-info">
                <button type="button" class="close" data-dismiss="alert" aria-hidden="true">
                    ×</button>
                <span class="glyphicon glyphicon-info-sign"></span> <strong>Info Message</strong>
                <hr class="message-inner-separator">
                <p>
                    This alert needs your attention, but it's not super important.<br> if you don't see this page it means your account is not deleted </p>
            </div>
        </div>
        <div class="col-sm-6 col-md-6">
            <div class="alert alert-warning">
                <button type="button" class="close" data-dismiss="alert" aria-hidden="true">
                    ×</button>
                <span class="glyphicon glyphicon-record"></span> <strong>Message</strong>
                <hr class="message-inner-separator">
                <p>
                    thanks for corparate with us</p>
            </div>
        </div>
        <div class="col-sm-6 col-md-6">
            <div class="alert alert-danger">
                <button type="button" class="close" data-dismiss="alert" aria-hidden="true">
                    ×</button>
                <span class="glyphicon glyphicon-hand-right"></span> <strong>Message</strong>
                <hr class="message-inner-separator">
                <p>
                    if you face nay prblem plz contact with us </p>
            </div>
        </div>
    </div>
</div>

        """)