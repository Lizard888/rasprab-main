import datetime
import re
import calendar

import mysql.connector
from mysql.connector import Error

import pdb
import mysql.connector
#ld=["1"]

 
  #global ld
  #print('ld=',ld)
ur=[]
now = datetime.datetime.now()



ye=int(now.year)

chas=int(now.hour)


mi=int( now.minute)

mes=int(now.month)
chis=int(now.day)

post=0
nomden=calendar.weekday(ye,mes,chis)
#print('nomden=',nomden)
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


n=0
cur = conn.cursor()
#pdb.set_trace() 

#chasi=chas
chasi=9
mi=45
nasden1=nomden+1
ur={}


ld=[]
query = ("SELECT * FROM %s" % den) #работает
cur.execute(query)



kkk1=[]
kkk2=[]
kkk3=[]

print('den=',den)
for (n) in cur:
    
  
      kkk2.append(n[2])
      kkk1.append(n[1])
      kkk3.append(n[3])
    
    
        
print(kkk1)
print(kkk2)
print(kkk3)
le=len(kkk2)
if int(kkk2[le-1])==chasi:
  if abs(int(kkk3[le-1])- mi)>=2: ld.append('Go home')
  
#if abs(int(kkk2[le-1])-chasi)>4:#den=kalen.get(nomden+1) следующий день
#pdb.set_trace() 
i=0
zz=0
lld=0
#pdb.set_trace()
print(type(mi))
if  int(kkk2[i])>=chasi:
          ld=kkk1

else:
 
 lld=kkk2.index(str(chasi))
 
 i=lld
 
 if abs(int(kkk3[i])-mi)>2 and int(kkk3[i])<mi:  i=lld+1
     
 elif  abs(int(kkk3[i])-mi)<=2 and int(kkk3[i])>mi: i=lld 
 while i!=le:
    ld.append(kkk1[i])
    i=i+1

   # else:     
   

          
    # elif abs(int(kkk3[i])-mi)>2:
        
     #else: i=i+1        

print(ld)

#def shet():
  #ld.append(kkk1[i])
#  i=i+1   





   
