import sqlite3

conn = sqlite3.connect('c://html.db')
cur = conn.cursor()

conn.execute('DROP TABLE IF EXISTS html ')
conn.execute("CREATE TABLE Html(\
    ID INTEGER PRIMARY KEY AUTOINCREMENT,\
    DESCRIPTION TEXT);")

conn.close()
