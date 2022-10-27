
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route,get,post, template, request,redirect
import sqlite3


connection = sqlite3.connect("shopping_list.db")


@route('/')
def hello_world():
    return 'Hello from priyanka!'

@route('/hi')
def hello_world():
    return 'Hii from priyanka!'

@route('/bye')
def hello_world():
    return 'bye from priyanka!'

@route('/list')
def get_list():
    cursor = connection.cursor()
    rows = cursor.execute("select id, descrption from list")
    rows = list(rows)
    rows = [ {'id':row[0], 'desc':row[1]} for row in rows]
    return template("shopping_list.tpl", name="shin" , shopping_list=rows )


@get('/add')
def get_add():
    return template("add_item.tpl")

@post('/add')
def post_add():
    descrption = request.forms.get("descrption")
    cursor = connection.cursor()
    cursor.execute(f"insert into list (descrption) values ('{descrption}')")
    connection.commit()
    redirect('/list')

@route("/delete/<id>")
def get_delete(id):
    cursor = connection.cursor()
    cursor.execute(f"delete from list where id={id}")
    connection.commit()
    redirect('/list')

@get("/edit/<id>")
def get_edit(id):
    cursor = connection.cursor()
    items = cursor.execute(f"select descrption from list where id={id}")
    items = list(items)
    if len(items) != 1:
        redirect('/list')
    descrption = items[0][0]
    return template("edit_item.tpl", id=id, descrption=descrption)

@post("/edit/<id>")
def post_edit(id):
    descrption = request.forms.get("descrption")
    cursor = connection.cursor()
    cursor.execute(f"update list set descrption='{descrption}' where id={id}")
    connection.commit()
    redirect('/list')



application = default_app()

