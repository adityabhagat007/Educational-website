#!C:\Users\user\AppData\Local\Programs\Python\Python38\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="ardent_pr")
cur=db.cursor()
db.commit()
import matplotlib.pyplot as plt                       
from random import * 
import mpld3                                 
y=[]                                                  
x=['sell','profit','revenu','student left','rating']  
for i in range(5):                                    
    r=randint(1,10)                                   
    y.append(r)                                       
plt.xlabel('subjects')                                
plt.ylabel('rate')                                    
plt.title('every day rates')                          
plt.bar(x,y, width=0.3)                               
plt.grid(True , color='b')                            
plt.savefig('C:\xampp\htdocs\ardent project/ graph1.png', dpi=300,bbox_inches='tight')
plt.show()
  print("""
  <html>
  <body>
  <img src="a3.png">
  </body>
  </html>
""") 