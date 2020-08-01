#Created by Veornica Vitale on 8 July 2020
#Server using bottle

from bottle import get, route, run, Bottle, static_file, view, request, redirect,view
import bottle
import json
import database

#these will be used when accounts for resturaunts are made
import bcrypt
import random
import hashlib
import mysql.connector

app = Bottle()
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "m-and-t"
    )

mycursor = mydb.cursor()
#base of where all static pages are served from
file_root = "../frontend"
#base of where all templates are served from
bottle.TEMPLATE_PATH.insert(0, "../frontend")
#resets templates between server restarts
bottle.TEMPLATES.clear()
#serves the home page where users may look up a restuarnt
@app.get('/')
def serve_home():
	return static_file("search.html", root=file_root, mimetype="text/html")
#servers the login for the restuarnt
@app.get('/login')
def serve_login():
	return static_file("login.html", root=file_root, mimetype="text/html")


@app.post('/results')
@view("results.tpl")
def serve_search():
 	"""
 	Template foramt
 	a dictionary with one key resturants
 	resturants is a list of lists
 	 the frist element of each list is the name, the second is the description and the third is the id
 	"""

 	msg = request.forms("query")


 	retVal = {"restuarunt": []}

 	retVal = database.searchRestaurant(msg)

 	return retVal


#serves the restuarunt's menu

@app.get('/m/<resturant_name>')
@view("view-menu.tpl")
def serve_resturant(resturant_name):
	"""
	Template format

	a dictionary with the keys name and items
	name  holds a string, which is the name of the restuarnt
	items holds dictionary of lists
		each key is a section header
		each list contains tuples that has the item and price of each item and a description
	"""
	retVal = database.searchRestaurantId(resturant_name)
	return retVal

	

#allows the restuarant to edit their menu

#NEED TO VERIFY THE USER HAS LOGGED IN
@app.get('/e/<resturant_name>')
@view("menu.tpl")
def serve_resturant_edits(resturant_name):
	"""
	Template format

	a dictionary with the keys name and items
	name  holds a string, which is the name of the restuarnt
	items holds dictionary of lists
		each key is a section header
		each list contains tuples that has the item and price of each item and a description
	section holds the sections with their corresponding section id
	"""
	#Call to Database
	retVal = database.searchRestaurantId(resturant_name)
	return retVal

@app.get('/style.css')
def serve_style():
	return static_file("style.css", root=file_root, mimetype="text/css")

@app.get('/ajax.js')
def serve_ajax():
	return static_file("ajax.js", root=file_root, mimetype="text/javascript")

@app.get('/edit.js')
def serve_ajax():
	return static_file("ajax.js", root=file_root, mimetype="text/javascript")

@app.post("/login-confirm")
def confirmLogin():
    username = request.forms["user"]
    password = request.forms["passwd"]
    select = "SELECT * FROM users WHERE username= %s"
    mycursor.execute(select, (username,))
    row = mycursor.fetchone()
    if row is not None:
        if bcrypt.checkpw(str(password).encode('utf-8'), str(row[2]).encode('utf-8')):
            redirect('/e/<resturant_name>')
        else:
            return "Incorrect credentials."
    else:
        redirect('/register')

@app.post("/register-process")
def processRegister():
    username = request.forms["username"]
    password = request.forms["password"]
    # # this is where you should check if password meets criteria
    # # if it does hash the pw and store it in the database
    select = "SELECT * FROM users WHERE username= %s"
    mycursor.execute(select, (username,))
    row = mycursor.fetchone()
    if row is not None:
        return "Username already in use."
    if len(username) < 5:
        return "Username is too short."
    if len(username) > 20:
        return "Username is too long."

    if checkCriteria(str(password)) == "valid":
        hashedpw = saltAndHash(password)
        hashedpw = str(hashedpw.decode('utf-8'))
        reg_stmt = (
        "INSERT INTO users (username, password) "
        "VALUES (%s, %s)"
        )
        reg_val = (username, hashedpw)
        mycursor.execute(reg_stmt, reg_val)
        mydb.commit()

        mycursor.execute("SELECT id FROM users WHERE username = %s AND password = %s", (username, hashedpw))
        result = mydb.fetchone()

        mycursor.execute("INSERT INTO restaurant(name, user_id, description) VALUES (%s, %s, %s)", ("Restaurant", "Description goes here", result[0]))
        mydb.commit()

        mycursor.execute("SELECT LAST_INSERT_ID();")
        res = mydb.fetchone()

        # print("if this is not one number ummm make it that way: " res)

        redirect('/e/<resturant_name>')
    else:
        return checkCriteria(str(password))

@app.get("/register")
def serveRegister():
    return static_file("register.html", root=file_root, mimetype="text/html")

@app.get("/restaurant")
def serveRegister():
    return static_file("restaurant_setup.html", root=file_root, mimetype="text/html")

@app.post("/restaurant-setup")
def processRegister():
	restaurant = request.forms["restaurant"]
	description = request.forms["description"]
	# # this is where you should check if password meets criteria
	# # if it does hash the pw and store it in the database
	# insert = "INSERT INTO restaurant (name, description) VALUES (restaurant, description)"
	insert = ("INSERT INTO restaurant (name, description) VALUES ({},{})".format(restaurant,description))
	mycursor.execute(insert)
	mydb.commit()
	return

@app.post("/restaurant-search")
def processRegister():
	res_name= request.forms["resName"]
	print(res_name)
	# # this is where you should check if password meets criteria
	# # if it does hash the pw and store it in the database
	# insert = "INSERT INTO restaurant (name, description) VALUES (restaurant, description)"
	select = ("SELECT * FROM restaurant WHERE name = %s", (res_name))
	mycursor.execute(select)
	row = mycursor.fetchone()
	mydb.commit()
	print(row)
	redirect('/e/<resturant_name>')

def checkCriteria(password):
    if len(password) < 8:
        return "Password must be at least 8 characters."
    if len(password) > 255:
        return "Password has too many characters."
    if password.islower():
        return "Password must contain an uppercase character."
    if not any(char.isdigit() for char in password):
        return "Password must contain a number."
    return "valid"

def saltAndHash(password):
    hashedpw = bcrypt.hashpw(str(password).encode('utf-8'), bcrypt.gensalt())
    return hashedpw

@app.post('/addItem')
def serve_newItem():
	section = {}
	section["name"] = request.forms["item"]
	section["price"] = request.forms["Price"]
	section["description"] = request.forms["Desc"]
	section["id"] = request.forms["sid"]

	retVal = database.addItem(section)

	return json.dumps(retVal)
	

@app.post('/addSection')
def serve_newSection():
	section = {}
	rid = request.forms["rid"]
	sectionName = request.forms["section"]
	
	retVal = database.addSection(section)

	return json.dumps(retVal)

@app.post("/removeItem")
def serve_removeItem():
	req = request.body.read()
	data = json.loads(req)

	database.delectionItem(data)

	return "deleted"

@app.post("/removeSection")
def serve_removeSection():
	req = request.body.read()
	data = json.loads(req)

	database.delelteSection(data)

	return "deleted"

@app.post("/updateDesc")
def serve_updateDesc():
	req = request.body.read()
	data = json.loads(req)

	database.updateRestaurantdescription(data["id"], data["description"])

	return "updated"

@app.post("/updateName")
def serve_updateDesc():
	req = request.body.read()
	data = json.loads(req)

	database.updateRestaurantdescription(data["id"], data["name"])

	return "updated"

app.run(host='localhost', port=8080)