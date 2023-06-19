import sqlite3


def save_data(inssa):

    con = sqlite3.connect('database.db')

    cursor = con.cursor()
    sql = '''
    INSERT INTO geni (title, artist)
    VALUES (?, ?)
    '''
    cursor.executemany(sql, inssa)
    con.commit() 
    con.close() 


def get_data():

    con = sqlite3.connect('database.db')

    cursor = con.cursor() 

    sql = '''
    SELECT * FROM geni
    '''
    cursor.execute(sql)


    all_data = cursor.fetchall()

    con.close()
    return all_data

def create_tb():
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

def drop_tb():
    con = sqlite3.connect('database.db')
    cursor = con.cursor() 
    sql = '''
        DROP TABLE geni
    '''
    cursor.execute(sql)
    con.commit()
    con.close()  