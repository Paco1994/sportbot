from pony.orm import *
from datetime import *
from sportbot import config

db = Database()

# Clases

from sportbot.model import user

# Fin clases

db.bind('sqlite', '../../config/data.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
