# -*- coding: utf-8 -*-

import telebot # Librería de la API del bot.
import random
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

TOKEN = '163718613:AAHUpvFTGS2xkmHQsIDKzWe4uEnlLsBQFrQ' # Nuestro tokken del bot (el que @BotFather nos dió).

bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
local = True
gif = "https://lachatupdate.files.wordpress.com/2015/08/547b7a894bcc7.gif"
usuarios = [line.rstrip('\n') for line in open('usuarios.txt')] #cargamos la lista de usuarios
administrador = 14550586

def listener(messages):
    for m in messages:
        cid = m.chat.id
        mensaje = ""
        if m.content_type == 'text': # Sólo saldrá en el log los mensajes tipo texto
            if cid > 0:
                mensaje = str(m.chat.first_name) + "[" + str(cid) + "]: " + m.text
                f = open('sources/log.txt', 'a')
                f.write(mensaje + "\n")
                f.close()
                print mensaje
            else:
                if m.text[0] == '/':
                    mensaje = str(m.from_user.first_name) + "[" + str(cid) + "]: " + m.text 
                    f = open('sources/log.txt', 'a')
                    f.write(mensaje + "\n")
                    f.close()
                    print mensaje

bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.



bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.