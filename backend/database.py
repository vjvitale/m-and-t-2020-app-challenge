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
    #hash password before entering into database
    my_cursor.execute("")

def delectionItem(item):
    

def deleteSection(section):


def searchRestaurant(resturant_name):
    retVal = {}
    sectionItems = {}
    my_cursor.execute("SELECT name, id FROM restaurant WHERE name == resturant_name")
    result = mycursor.fetchall()
    if len(result[0]) == 0:
        return nil
    else:
        idList = result[1]
        for r in range(0, len(idList)):
            rid = idList[r]
            my_cursor.execute("SELECT name, id FROM section WHERE id == rid")
            section_result = mycursor.fetchall()

            for i in range(0, len(section_result[1])):
                sId = section_result[1][i]
                my_cursor.execute("SELECT name, price, description FROM menu-item WHERE id == sId")
                items = mycursor.fetchall()
                sectionName = section_result[0][i]
                sectionItems[sectionName] = items

            resName = result[0][r]
            retVal[resName] = sectionItems
        
        return retVal
        


# query = SELECT name FROM table_name;