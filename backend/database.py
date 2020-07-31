import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "m-and-t"
    )

my_cursor = mydb.cursor()
# my_cursor.execute("")

def loginUser(username, password):
    password = password.encode()
    salt = os.urandom(16)
    password_hash = hashlib.pbkdf2_hmac("sha256", password, salt, 100000)
    my_cursor.execute("INSERT INTO users (username, password) VALUES (username, password_hash)")

def delectionItem(item_id):

    my_cursor.execute("DELETE FROM menu-item WHERE id = %s", (item_id))
    

def deleteSection(s_id):
    #Need to implement backend part
    
    my_cursor.execute("DELETE FROM menu-item WHERE section_id = %s", (s_id))
    my_cursor.execute("DELETE FROM section WHERE section_id = %s" (s_id))



def addItem(item):
    name = item["name"]
    price = item["price"]
    description = item["description"]
    iD = item["id"]
    
    my_cursor.execute("INSERT INTO menu-item (name, price, description, section_id) VALUES (name, price, description, iD)")
    my_cursor.execute("SELECT id FROM menu-item WHERE name = %s AND price = %s AND description = %s AND section_id = %s", (name, price, description, iD))
    item_id = my_cursor.fetchall()

    return {"item" : name, "price": price, "description": description, "item_id": item_id[0][0]}

def addSection(section):
    name = section["section"]
    res = section["res_id"]

    my_cursor.execute("INSERT INTO section (name, restaurant_id) VALUES (name, res)")
    my_cursor.execute("SELECT id FROM section WHERE name = %s AND restaurant_id = %s", (name, res))
    sect_id = my_cursor.fetchall()

    return {"section": name, "sid": sect_id}

def searchRestaurant(resturant_name):
    retVal = {"restaurant": []}
    sectionItems = {}
    my_cursor.execute("SELECT name, id, description FROM restaurant WHERE name == resturant_name")
    result = my_cursor  .fetchall()
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
    my_cursor.execute("SELECT name FROM restaurant WHERE id == rid")
    result = my_cursor.fetchall()
    my_cursor.execute("SELECT name, id FROM section WHERE restaurant_id == rid")
    section_result = my_cursor.fetchall()

    for i in range(0, len(section_result[1])):
        sId = section_result[1][i]
        my_cursor.execute("SELECT name, price, description FROM menu-item WHERE section_id == sId")
        items = my_cursor.fetchall()
        sectionName = section_result[0][i]
        sectionItems[sectionName] = items

    retVal["name"] = result[0][1]
    retVal["items"] = sectionItems
    retVal["sections"] = {}
    retVal["restaurant_id"] = rid

    for sec in range(len(section_result[0])):
        retVal["sections"][section_result[0][sec]] = section_result[1][sec]

    return retVal