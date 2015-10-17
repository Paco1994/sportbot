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
usuarios = [line.rstrip('\n') for line in open('sources/usuarios.txt')] #cargamos la lista de usuarios
administrador = '43748337'

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

@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if str(cid) in usuarios:
        bot.send_message( cid, "Ya estás registrado como usuario del ASL Sports Bot." )
    else: # Con esta sentencia, hacemos que solo se ejecute lo de abajo cuando un usuario hace uso del bot por primera vez.
        usuarios.append(str(cid)) # En caso de no estar en la lista de usuarios, lo añadimos.
        f = open( 'sources/usuarios.txt', 'a') # Y lo insertamos en el fichero 'usuarios.txt'
        f.write( str(cid) + "\n")
        f.close()
        bot.send_message( administrador, "Se ha registrado el ID " + str(cid))
        #USERFILE = "users/" + str(cid) + ".txt"
        #f = open( USERFILE, 'w')
        #f.close()
        if cid < 0:
            bot.send_message( cid, "Bienvenidos. Este grupo se ha registrado en ASL Sports Bot.")
        else:
            bot.send_message( cid, "Bienvenido. Te has registrado en ASL Sports Bot. Elige tu equipo favorito.")
			#ELEGIR EQUIPO.

bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.
