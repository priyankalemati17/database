import sqlite3
connection=sqlite3.connect("shopping_list.db")
cursor=connection.cursor()
try:
    cursor.execute("drop the list")
except:
    pass
cursor.execute("create table list(id integer primary key,descrption text)")
cursor.execute("insert into list(descrption) values ('apples')")
cursor.execute("insert into list(descrption) values ('oranges')")
cursor.execute("insert into list(descrption) values ('grapes')")
cursor.execute("insert into list(descrption) values ('pineapple')")
cursor.execute("insert into list(descrption) values ('kiwi')")
connection.commit()
connection.close()
print()