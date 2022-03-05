
import mysql.connector
from mysql.connector import Error

import pdb
import mysql.connector

kalen={}
kalen={0:"mondey",
         1:"tuesday",
         2:"wednesday",
         3:"thursday",
         4:"friday"}
#den=kalen.get(nomden)
den="wednesday"

try:
    conn = mysql.connector.connect(
         user='root',
         #password='lizard',
         host='localhost',
         database='rasp')
    if conn.is_connected():
            print('Connected to MySQL database')

except Error as e:
  print('e=',e)




ss=0


while ss!=2:
  n=0
  cur = conn.cursor()
  if ss==1: den="friday"
 
  
  query = ("SELECT * FROM %s" % den) #работает
  cur.execute(query)
  kkk1=[]
  kkk2=[]
  kkk3=[]
 
  for (n) in cur:
      kkk2.append(n[2])
      kkk1.append(n[1])
      kkk3.append(n[3])
  print(kkk1)
  print(kkk2)
  print(kkk3)
  ss=ss+1
      
  
