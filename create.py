import sqlite3
con = sqlite3.connect('database.db')
print(type(con))
cursor = con.cursor()

sql = '''
CREATE TABLE "geni" (
    "rank"    INTEGER NOT NULL,
    "title"  TEXT NOT NULL,
    "artist"  TEXT NOT NULL,
    PRIMARY KEY("rank" AUTOINCREMENT)
)
'''

cursor.execute(sql) 
con.commit() 
con.close()  