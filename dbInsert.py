import mysql.connector
import datetime
dataBase = mysql.connector.connect(
host ="localhost",
user ="root",
passwd ="admin",
database="Supplychain"
)
cursorObject = dataBase.cursor()




# sql = "INSERT INTO CLOTH (CLOTH_ID,NAME,SIZE,TYPE,PRICE) VALUES (%s,%s, %s,%s,%s)"
# val = (1 ,"fahad" ,"s",  "men",1200)
# cursorObject .execute(sql, val)
# val1 = (2 ,"Ali" ,"m",  "men",1300)
# cursorObject .execute(sql, val1)
# val2 = (3 ,"Abeeha" ,"l",  "girl",1500)
# cursorObject .execute(sql, val2)


# sql1 = "Insert into Distributor(Distributor_ID,name,contact,warehouse_Address,city) values (%s,%s,%s,%s,%s)"
# dis1 = (101, "Javed",31332,"bahadurabad","karachi")
# cursorObject .execute(sql1, dis1) 
# dis2 = (102, "Ahmed",34355,"bahira town","Lahore")
# cursorObject .execute(sql1, dis2)
# dis3 = (103, "Jawwad",31334,"Dhoodiyal","Mansehrah") 
# cursorObject .execute(sql1, dis3)
# dataBase.commit()
# sql2 = "Insert into Client(Client_ID,name,contact,shop_Address,city) values (%s,%s,%s,%s,%s)"
# C1 = (181, "Kazi",31332,"defense","karachi")
# cursorObject .execute(sql2, C1) 
# C2 = (182, "Ahmed",34355,"Faisal Town","Lahore")
# cursorObject .execute(sql2, C2)
# C3 = (183, "Jawwad",31333,"Lari adda","Mansherah") 
# cursorObject .execute(sql2, C3)
# dataBase.commit()
sql3 = "Insert into Transport_Employee(Emp_ID,name,Distributor_ID) values (%s,%s,%s)"
TE1 = (191, "qamar",101)
cursorObject .execute(sql3, TE1) 
TE2 = (192, "Albert",102)
cursorObject .execute(sql3, TE2)
TE3 = (193, "Tom",101) 
cursorObject .execute(sql3, TE3)


sql4 = "Insert into Stock(Distributor_ID,quantity,CLOTH_ID) values (%s,%s,%s)"
S1 = (101, 200,2)
cursorObject .execute(sql4, S1) 
S2 = (102, 300,1)
cursorObject .execute(sql4, S2)
S3 = (103, 349,1) 
date1 = datetime.datetime(2022,2,27)
str_date1 = date1.date().isoformat()
date2 = datetime.datetime(2022,6,23)
str_date2 = date2.date().isoformat()
date3 = datetime.datetime(2022,2,20)
str_date3 = date3.date().isoformat()
sql5 = "Insert into Supply(Client_ID,CLOTH_ID,quantity,Employee_ID,date) values (%s,%s,%s,%s,%s)"
SU1 = (181,1,14,191,str_date1)
cursorObject .execute(sql5, SU1) 
SU2 = (182,2,10,192,str_date2)
cursorObject .execute(sql5, SU2)
SU3 = (183,1,20, 191,str_date3) 
cursorObject .execute(sql5, SU3)
dataBase.commit()