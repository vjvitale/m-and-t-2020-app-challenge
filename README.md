## Running the Server
To run the server go navagate to the systems root folder.

From there cd into the backend folder. You will need bottle, and bcrypt installed if you don't already have it on your device.

To install run the command

`pip install bcrypt` , and `pip install bottle`

Once the dependecies are finished being installed, type the command `python server.py`

This will run the server. You can then go to the url http://localhost:8080, http://localhost:8080/e or http://localhost:8080/m to access the pages for the site.

The database is in MySQL in which the 

## Features

Our site is split between consumers and resturant owners. In doing this, it allows for owners to update their menus and add any new items. Customers can then view these items
that the owners put on. On the menu, an item is listed under a section. For example you can have drinks, breakfast, etc. This allows seperation between all the items
on the menu and makes it look more like a menu one would see at the resturant. Owners can login into the site to access and change the menu up by deleting an item, section or
adding an item or section. 
