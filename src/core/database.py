from contextvars import ContextVar
import peewee
from peewee import  MySQLDatabase
from playhouse.pool import PooledMySQLDatabase

from src.config.config import settings

db_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())


class PeeweeConnectionState(peewee._ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]


async def reset_db_state():
    db._state._state.set(db_state_default.copy())
    db._state.reset()


db = MySQLDatabase(
    database=settings.DB.DB_DATABASE,
    user=settings.DB.DB_USER,
    host=settings.DB.DB_HOST,
    password=settings.DB.DB_PASSWORD,
    port=settings.DB.DB_PORT
)

db._state = PeeweeConnectionState()

