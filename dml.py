import mysql.connector
import datetime
dataBase = mysql.connector.connect(
host ="localhost",
user ="root",
passwd ="admin",
database="Supplychain"
)
cursorObject = dataBase.cursor()
e = 2
query1 = "SELECT s.quantity,d.name from stock s inner join distributor d on s.distributor_id = d.distributor_id where d.distributor_id = {}".format(e)
cursorObject.execute(query1)

query2="SELECT distributor_id from stock"
cursorObject.execute(query2)