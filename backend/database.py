import mysql.connector


 """
  IMPORTANT: RESTAURANTS NEED DESCRITPTIONS, 
 """


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "m-and-t"
    )

my_cursor = mydb.cursor()
# my_cursor.execute("")

def loginUser(username, password):
    #hash password before entering into database
    my_cursor.execute("INSERT INTO users (username, passwoerd) VALUES (username, password)")

def delectionItem(item):
    name = item["name"]
    price = item["price"]
    description = item["description"]
    my_cursor.execute("DELETE FROM menu-item WHERE name == name AND price == price AND description == description")
    

def deleteSection(section):
    #Need to implement backend part
    name = section["name"]
    id = section["id"]
    my_cursor.execute("DELETE FROM menu-item WHERE section_id == id")
    my_cursor.execute("DELETE FROM section WHERE name == name AND id == id")

def addItem(item):
    name = item["name"]
    price = item["price"]
    description = item["description"]
    id = item["id"]
    
    my_cursor.execute("INSERT INTO menu-item (name, price, description, section_id) VALUES (name, price, description, id)")

def addSection(section):
    name = section["section"]
    res = section["res_id"]

    my_cursor.execute("INSERT INTO section (name, restaurant_id) VALUES (name, res)")

def searchRestaurant(resturant_name):
    retVal = {"restaurant": []}
    sectionItems = {}
    my_cursor.execute("SELECT name, id, description FROM restaurant WHERE name == resturant_name")
    result = mycursor.fetchall()
    if len(result[0]) == 0:
        return retVal
    else:
        idList = result[1]
        for r in range(0, len(idList)):
            retVal["restaurant"].append([result[0][r], idList[r]], result[2][r])
            
        
        return retVal

def searchRestaurantId(rid):
    retVal = {}
    sectionItems = {}

    mycursor.execute("SELECT name FROM restaurant WHERE id == rid")
    result = mycursor.fetchall()



    my_cursor.execute("SELECT name, id FROM section WHERE restaurant_id == rid")
    section_result = mycursor.fetchall()

    for i in range(0, len(section_result[1])):
        sId = section_result[1][i]
        my_cursor.execute("SELECT name, price, description FROM menu-item WHERE section_id == sId")
        items = mycursor.fetchall()
        sectionName = section_result[0][i]
        sectionItems[sectionName] = items

    retVal["name"] = result[0][1]
    retVal["items"] = sectionItems
    retVal["sections"] = {}

    for sec in range(len(section_result[0])):
        retVal["sections"][section_result[0][sec]] = section_result[1][sec]

    return retVal