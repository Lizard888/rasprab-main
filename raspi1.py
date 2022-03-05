import telebot
import configparser
import json
from telebot import apihelper
import datetime
import re
import calendar
from datab11e import bazad
#global ld
#ld=[]
Token1="5153409742:AAE-CeeF-nowya8PefXs5qm4_Vqu8xCSZeo"# Uroki
bot = telebot.TeleBot(Token1)
@bot.message_handler(commands=['start'])
def start_command(message):
  
   ld=[]
   bazad(ld)
   i=0
   print(ld)
   for (i) in  ld:
         bot.send_message(  message.chat.id,i)
         print(i)
bot.polling()
