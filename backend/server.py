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
#serves the home page where users may look up a restuarnt
@app.get('/')
def serve_home():
	return static_file("index.html", root="ADD ROOT FOR HTML", mimetype="text/html")
#servers the login for the restuarnt
@app.get('/login')
def serve_login():
	return static_file("login.html", root="ADD ROOT FOR HTML", mimetype="text/html")

#serves the restuarunt's menu

#THIS WILL BE A TEMPLATE
@app.get('/r/<resturant_name>')
def serve_resturant(resturant_name):
	return "RETURN THE TEMPLATE"

#allows the restuarant to edit their menu

#THIS WILL ALSO BE A TEMPLATE
#NEED TO VERIFY THE USER HAS LOGGED IN
@app.get('/e/<resturant_name>')
def serve_resturant(resturant_name):
	return "RETURN THE TEMPLATE"

app.run(host='localhost', port=8080)