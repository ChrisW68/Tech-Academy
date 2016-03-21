import sqlite3, db_program74

html_Values=(
    ('1'),
    ('2'),
    ('3')
)

with sqlite3.connect('html_database.db')as connection:
    c=connection.cursor()
c.execute("DROP TABLE IF EXISTS Html")
c.execute("CREATE TABLE Html(Description TEXT)")
c.executemany("INSERT INTO Html VALUES(?)", html_Values)
for row in c.fetchall():
    print(row)
