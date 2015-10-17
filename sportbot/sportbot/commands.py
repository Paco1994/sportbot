# -*- coding: utf-8 -*-
from sportbot import bot
from sportbot.models import users
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from pony.orm import *

import livescore
from livescore import *
import partidosweb
from partidosweb import elimina_tildes


@bot.message_handler(commands=['start'])
@db_session
def command_start(m):
    cid = m.chat.id
    bot.send_message("Utiliza el comando /partido [Nombre equipo] para saber el resultado de este equipo")
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

@bot.message_handler(commands=['partido'])
def command_setequipo(m):
    equipo = m.text[9:]
    cid = m.chat.id
    listadoURLs = ini2urls("sportbot/url.ini",0)    # Lectura de URL desde fichero de INICIO
    keys, vlr = listadoURLs.claves_valores()  # Claves y valores
    listadoURLs.listado()
    ls = LiveScore(keys, vlr)
    print (len(ls.partidos))
    equipo=elimina_tildes(equipo,False)
    pts = ls.buscar(equipo)
    for pt in pts:
        bot.send_message ( cid, str(pt) )
