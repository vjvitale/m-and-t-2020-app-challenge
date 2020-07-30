#Created by Veornica Vitale on 8 July 2020
#Server using bottle

from bottle import get, route, run, Bottle, static_file, view, request
import bottle
import json

#these will be used when accounts for resturaunts are made
import bcrypt
import random
import hashlib

app = Bottle()
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
	retVal = {"name" : "", "items":{}}

	retVal["name"] = "Eggs Dee"
	retVal["items"] = {"Drinks": [("soda", "2.50", "Choices of Pepsi Products"), ("tea", "1.50", "Choices of Chai, Green, or Black")], "Main Courses": [("Omlet", "7.99", "Eggs choice of tomatoes, mushrooms"), ("Eggs Benedict", "15.00", "Poached eggs on an english muffin with canadian bacon and hollandaise sauce")]}
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
	"""
	#Call to Database
	retVal = {"name" : "", "items":{}}

	retVal["name"] = "Eggs Dee"
	retVal["items"] = {"Drinks": [("soda", "2.50", "Choices of Pepsi Products"), ("tea", "1.50", "Choices of Chai, Green, or Black")], "Main Courses": [("Omlet", "7.99", "Eggs choice of tomatoes, mushrooms"), ("Eggs Benedict", "15.00", "Poached eggs on an english muffin with canadian bacon and hollandaise sauce")]}
	return retVal

@app.get('/style.css')
def serve_style():
	return static_file("style.css", root=file_root, mimetype="text/css")

app.run(host='localhost', port=8080)