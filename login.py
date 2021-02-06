#!C:\Users\user\AppData\Local\Programs\Python\Python38\python.exe
print("Content-type:text/html\r\n\r\n")
import mysql.connector
import time
t=time.time()
a=time.localtime()
import cgi
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="ardent_pr")
cur=db.cursor()
form=cgi.FieldStorage()
u=form['username'].value
p=form['password'].value
cur.execute("select * from student where username='{0}'".format(u))
x=cur.fetchone()
db.commit()
for i in range(len(x)):
    n=x[0]
    co=x[4]
    st=x[1]
    ag=x[3]
    e=x[2]
    us=x[6]
    numb=x[5]
    ps=x[7]
if p==ps and u==us:

    
    print('<h2><u>WELCOME</u></h2>', n)
    print("""
        <link href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
       <script src="//netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js"></script>
       <script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
        <!------ Include the above in your HEAD tag ---------->

        <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" type="text/css" rel="stylesheet">

      <div id="top-nav" class="navbar navbar-inverse navbar-static-top">
      <div class="container-fluid">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="#">Dashboard</a>
        </div>
        <div class="navbar-collapse collapse">
            <ul class="nav navbar-nav navbar-right">
                <li class="dropdown">
                    <a class="dropdown-toggle" role="button" data-toggle="dropdown" href="#"><i class="fa fa-user-circle"></i><span class="caret"></span></a>
                    <ul id="g-account-menu" class="dropdown-menu" role="menu">
                        <li><a href="#"><i class="fa fa-user-secret"></i> My Profile</a></li>
                    </ul>
                </li>
                <li><a href="web1.html"><i class="fa fa-sign-out"></i> Logout</a></li>
            </ul>
        </div>
    </div>
    <!-- /container -->
    </div>
    <!-- /Header -->

   <!-- Main -->

    <div class="col-lg-2 col-md-2 col-sm-3 col-xs-12">

    <ul class="nav nav-pills nav-stacked" style="border-right:1px solid black">
        <!--<li class="nav-header"></li>-->
        <li><a href="update.py?username={0}&name={1}&course={2}&number={3}&email={4}"><i class="fa fa-dashboard"></i> Update</a></li>
        <li><a href="delete.py?username={5}&name={6}"><i class="fa fa-tags"></i>delete Account</a></li>
        <li><a href="contact.html"><i class="fa fa-history"></i>contact admin</a></li>
        <li><a href="payment.html"><i class="fa fa-lock"></i>Course Payment</a></li>
    </ul>
     </div><!-- /span-3 -->
    <div class="col-lg-10 col-md-10 col-sm-9 col-xs-12">
    <!-- Right -->

    <a href="#"><strong><span class="fa fa-dashboard"></span> My Dashboard</strong></a>
    <hr>
   </div>
   """.format(us,n,co,numb,e,us,n))
    print("""
        <html>
        <head>
        <title>view</title>
        </head>
        <h2>INFO</h2>
        <table border="3">
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
        <tr border>
        <tbody>
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
        </table>
        </body>
        </html> """.format(n,st,e,ag,co,numb,us,ps))
        
else:
    print("invalid")


