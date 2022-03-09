import datetime
import re
import calendar
from telebot import apihelper
import mysql.connector
from mysql.connector import Error
import re
import pdb
import mysql.connector
import configparser
import telebot
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
den=kalen.get(nomden)
#den="friday"    
try:
    
    conn = mysql.connector.connect(
         user='root',
         host='localhost',
         database='rasp')
    if conn.is_connected():
            print('Connected to MySQL database')

except Error as e:
  print('e=',e)


n=0
chasi=chas
#chasi=20
#mi=37

nasden1=nomden+1
ur={}


ld=[]

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
 #print(kalen)
 print('den2=',den)
 print('nomden1 =',nomden)
 if den=="saturday" or den=="sunday":
     chasi=8
     dd=1
 she=she+1

 kkk1=[]
 kkk2=[]
 kkk3=[]
 kkk4=[]
 cur = conn.cursor()
 query = ("SELECT * FROM %s" % den) #работает
 cur.execute(query)
 for (n) in cur:  
      kkk2.append(n[2])
      kkk1.append(n[1])
      kkk3.append(n[3])
      kk=str(n[1])+ " "+str(n[2])+" "+str(n[3])
      kkk4.append(kk)
 print(kkk4)     
 print('oldden=',den)         
 print(kkk1)
 print(kkk2)
 print(kkk3)
 le=len(kkk2)
 #pdb.set_trace()
 print('dd=',dd)
 if int(kkk2[le-1])==chasi and abs(int(kkk3[le-1])- mi)>=2 :ld.append('Go home') 
   #if abs(int(kkk3[le-1])- mi)>=2: ld.append('Go home')
 elif (chasi-int(kkk2[le-1]))>0 and (chasi-int(kkk2[le-1]))<4:
     ld.append('Go home')
     ld.append('come back later')
 elif (chasi-int(kkk2[le-1]))>=4 and dd==0:
   print(kkk2[le-1])
   print(chasi)  
   print('dd1=',dd)
   den=kalen.get(nomden+1)# следующий день
   print('den2=',den)
   print('newden=',den)
   dd=1
   chasi=8
   vibor()
 
 else:
  i=0
  zz=0
  lld=0
 #pdb.set_trace()
  print(type(mi))
  if  int(kkk2[i])>=chasi:
          #ld=kkk1
           ld=kkk4
           
  else:
  #pdb.set_trace()   
    lld=kkk2.index(chasi)
 
    i=lld
 
    if abs(int(kkk3[i])-mi)>2 and int(kkk3[i])<mi:  i=lld+1
     
    elif  abs(int(kkk3[i])-mi)<=2 and int(kkk3[i])                                                                                                                                                                                                                                                                                                                                                                                         >mi: i=lld 
    while i!=le:
     #ld.append(kkk1[i])
     ld.append(kkk4[i])  
     i=i+1
   # print('she=',she)  
vibor()
     
print('she=',she)  
print(ld)
Token1="5153409742:AAE-CeeF-nowya8PefXs5qm4_Vqu8xCSZeo"# Uroki
bot = telebot.TeleBot(Token1)
@bot.message_handler(commands=['start'])
def start_command(message):
   i=0
   print(ld)
   for (i) in  ld:
         bot.send_message(  message.chat.id,i)
         print(i)
bot.polling()






   
