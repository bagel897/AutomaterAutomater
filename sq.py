import datetime
import sqlite3
from dataclasses import dataclass
import google
import google

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
queries_oop = []
for query in queries:
    queries_oop.append(state_change(query[0], query[1], query[2], query[3], query[4], query[5],
                                    query[6]))
for query in queries_oop:
    if query.domain == "light":
        print(query)
# queries = [query for query in queries]
# times = [query[6] for query in queries]
# print(queries[0])
# print(queries.__len__())
# cropped = queries[0:10]
# print(cropped)
# for query in queries:
#     if query[1] == "light":
#         print(query)
