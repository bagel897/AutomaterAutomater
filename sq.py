import datetime
import sqlite3
from dataclasses import dataclass
import tensorflow as tf


@dataclass
class state_change():
    state_id: int
    domain: str
    entity_id: str
    state: str
    attributes: dict
    event_id: int
    time: datetime.datetime


# from google.cloud import aiplatform
Filename = "haml/home-assistant_v2.db"
db = sqlite3.Connection(Filename)
queries = db.execute("SELECT * from states")


def read_db():
    for query in queries:
        yield [query[0], query[1], query[2], query[3], query[4], query[5], query[6]]


tf.data.Dataset.from_generator(read_db, output_types=(tf.int32, tf.int32, tf.string, tf.string,
                                                      tf.string, tf.string, tf.string))