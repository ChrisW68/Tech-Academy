import sqlite3


Description1 = 'High my name,  I forget'
Description2 = 'I think I remember'
Description3 = 'I forget'
with sqlite3.connect(':memory:') as connection:
    c=connection.cursor()

c.execute("DROP TABLE IF EXISTS Html")

c.execute("CREATE TABLE Html(Description TEXT Not Null)")

c.execute('''INSERT INTO Html (Description)
              VALUES(?)''', (Description1))
row=c.fetchall()
print(row)
