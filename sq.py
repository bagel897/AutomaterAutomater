import sqlite3
Filename = "haml/home-assistant_v2.db"
db = sqlite3.Connection(Filename)
queries = db.execute("SELECT * from states")
queries = [query for query in queries]
times = [query[6] for query in queries]
print(queries[0])
print(queries.__len__())
cropped = queries[0:10]
print(cropped)
