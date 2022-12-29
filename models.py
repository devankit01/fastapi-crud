from redis_om import get_redis_connection, EmbeddedJsonModel, JsonModel, Field, Migrator, HashModel
import datetime
from db_connection import redis



class Author(EmbeddedJsonModel):
    first_name: str = Field(index=True, full_text_search=True)
    last_name: str
    email: str
    date_joined: datetime.date = Field(default=datetime.datetime.now())

    class Meta:
        database = redis


class Blog(JsonModel):
    title: str = Field(index=True, full_text_search=True)
    content: str
    author: Author

    class Meta:
        database = redis


Migrator().run()
