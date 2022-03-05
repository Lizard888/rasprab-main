import datetime
import re
import calendar

import mysql.connector
from mysql.connector import Error

import pdb
import mysql.connector

ur=[]
now = datetime.datetime.now()



ye=int(now.year)

chas=int(now.hour)


mi=int( now.minute)

mes=int(now.month)
chis=int(now.day)

post=0
nomden=calendar.weekday(ye,mes,chis)

print('nomden=',nomden)
kalen={}
kalen={0:"mondey",
         1:"tuesday",
         2:"wednesday",
         3:"thursday",
         4:"friday",
         5:"saturday",
         6:"sunday"}
#den=kalen.get(nomden)
den="sunday"
#if den=="saturday" or den=="sunday":
   # den="mondey"
    
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
#cur = conn.cursor()

#chasi=chas
chasi=19
mi=45

nasden1=nomden+1
ur={}


ld=[]
#query = ("SELECT * FROM %s" % den) #работает
#cur.execute(query)



kkk1=[]
kkk2=[]
kkk3=[]
she=0
print('den=',den)
dd=0
def vibor():
 global kkk1
 global kkk2
 global kkk3
 global ld
 global chasi
 global den
 global she
 global dd
 global query
 global den
 global cur
 global nomden
 global kalen
 print(kalen)
 print('den2=',den)
 print('nomden1 =',nomden)
 if den=="saturday" or den=="sunday":
    den="mondey"
    chasi=8
    
 she=she+1
# pdb.set_trace()
 kkk1=[]
 kkk2=[]
 kkk3=[]
 

 cur = conn.cursor()
 query = ("SELECT * FROM %s" % den) #работает
 cur.execute(query)


 for (n) in cur:  
      kkk2.append(n[2])
      kkk1.append(n[1])
      kkk3.append(n[3])
 print('oldden=',den)         
 print(kkk1)
 print(kkk2)
 print(kkk3)
 le=len(kkk2)
 #pdb.set_trace()
 print('dd=',dd)
 
 if int(kkk2[le-1])==chasi:
   if abs(int(kkk3[le-1])- mi)>=2: ld.append('Go home')
 
 if abs(int(kkk2[le-1])-chasi)>=4 and dd==0:
   print(kkk2[le-1])
   print(chasi)
   
   print('dd1=',dd)
   den=kalen.get(nomden+1)# следующий день
   print('den2=',den)
   print('newden=',den)
   dd=1
  
   chasi=8
   vibor()

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
     
  elif  abs(int(kkk3[i])-mi)<=2 and int(kkk3[i])                                                                                                                                                                                                                                                                                                                                                                                         >mi: i=lld 
  while i!=le:
    ld.append(kkk1[i])
    i=i+1
  print('she=',she)  
vibor()
     
print('she=',she)  
print(ld)






   
