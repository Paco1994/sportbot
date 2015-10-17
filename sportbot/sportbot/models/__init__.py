from pony.orm import *
from datetime import *
from sportbot import config

db = Database()

# Clases

from sportbot.models import users

# Fin clases

db.bind('sqlite', '../../data.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
