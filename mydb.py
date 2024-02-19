import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd =""

)

cursorObject= dataBase.cursor()
cursorObject.execute("CREATE DATABASE dcrm")
print("All done!")


