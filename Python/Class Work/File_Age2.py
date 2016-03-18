import sqlite3

# Connect to Fix_Age Database
conn = sqlite3.connect('File_Age.db')


def createTable():
    conn.execute("CREATE TABLE if not exists FILEAGE_INFO (\
    ID INTEGER PRIMARY KEY AUTOINCREMENT,\
    AGE INT\
    );")


def printData(data):
    for row in Data:
        print("Id: "), row[0]
        print("Date: "), row[1]


def newFile(age):
    # Create values part of sql command
    val_str = "{}".format(age)

    sql_str = "INSERT INTO FILE_AGE_INFO (AGE) VALUES({});".format(val_str)

    print(sql_str)

    conn.execute(sql_str)
    conn.commit()
    return conn.total_changes


def viewAll():
    # Create sql string
    sql_str = "SELECT * from FILEAGE_INFO"
    cursor = conn.execute(sql_str)

    # Get data from cursor in Array
    rows = cursor.fetchall()
    return rows


def deleteFile():
    # Create sql string
    sql_str = "Delete from FILEAGE_INFO where ID={}".format(change_id)
    conn.execute(sql_str)
    conn.commit()
    return conn.total_changes


createTable()
