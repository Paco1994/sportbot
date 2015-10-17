from pony.orm import *
from sportbot.models import db

class User(db.Entity):
    """Clase User.
    Representa a un usuario de Telegram.
    """
    id = PrimaryKey(int, auto=False)
    equipo = Optional(str, nullable=True)
    last_name = Optional(str, nullable=True)
    #username = Optional(str, nullable=True)
@db_session
def search_user(user, team):
    """
    Busca y devuelve un usuario en la base de datos. Si no existe lo crea.
    """
    if select(u for u in User).filter(lambda x: x.id == user.id).exists():
        entity = User[user.id]
        entity.equipo = team
        entity.last_name = user.last_name
    else:
        entity = User(id=user.id,equipo=team, last_name=user.last_name)
        commit()

    return entity
