# -*- coding: utf-8 -*-
from sportbot import bot
from sportbot.models import users
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from pony.orm import *


@bot.message_handler(commands=['start'])
@db_session
def command_start(m):
    cid = m.chat.id
    #base=users.search_user(m.from_user)
    #print base.id
#u"Córdoba CF"

@bot.message_handler(commands=['eq'])
@db_session
def command_eq(m):
    cid = m.chat.id
    team = m.text[4:]
    usuario = users.search_user(m.from_user,team)
    print usuario.equipo

@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    help_text ="Estos son los comandos disponibles:\n"
    for i in commands:
        help_text += "/" + i + ": "
        help_text += commands[i] + "\n"
    bot.send_message( cid, help_text )

@bot.message_handler(commands=['setequipo'])
def command_setequipo(m):
    equipo = m.text[10:].title()
    cid = m.chat.id
    print "Añadido el equipo" + equipo
    USERFILE = "users/" + str(cid) + ".txt"
    f = open(USERFILE , 'a+r')
    if equipo not in f:
        f.write(equipo+"\n")
    else:
        bot.send_message(cid,"Ya tienes registrado este equipo " + equipo)
    f.close()
