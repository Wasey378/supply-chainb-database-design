# importing required libraries
import mysql.connector

dataBase = mysql.connector.connect(
host ="localhost",
user ="root",
passwd ="admin",
database="Supplychain"
)
cursorObject = dataBase.cursor()
 
# creating database
# creating table
CLOTH = """CREATE TABLE CLOTH (
                   CLOTH_ID INT PRIMARY KEY,
                   NAME  VARCHAR(20) NOT NULL,
                   SIZE VARCHAR(50) NOT NULL,
                   TYPE VARCHAR(5) NOT NULL,
                   PRICE INT NOT NULL
                   )"""
DISTRIBUTOR = """CREATE TABLE DISTRIBUTOR (
                DISTRIBUTOR_ID INT PRIMARY KEY,
                NAME  VARCHAR(20) NOT NULL,
                CONTACT INT,
                WAREHOUSE_ADDRESS VARCHAR(20),
                CITY CHAR(10) NOT NULL
)"""
CLIENT =  """CREATE TABLE  CLIENT(
                ClIENT_ID INT PRIMARY KEY,
                NAME  VARCHAR(20) NOT NULL,
                CONTACT INT,
                SHOP_ADDRESS VARCHAR(20),
                CITY CHAR(10) NOT NULL
)"""
TRANSPORT_EMPLOYEE =  """CREATE TABLE TRANSPORT_EMPLOYEE (
                EMP_ID INT PRIMARY KEY,
                NAME  VARCHAR(20) NOT NULL,
                DISTRIBUTOR_ID INT,
                FOREIGN KEY (DISTRIBUTOR_ID) REFERENCES DISTRIBUTOR(DISTRIBUTOR_ID)

)"""
STOCK =  """CREATE TABLE STOCK (
                DISTRIBUTOR_ID INT NOT NULL,
                QUANTITY  INT NOT NULL,
                CLOTH_ID INT NOT NULL,
                FOREIGN KEY (DISTRIBUTOR_ID) REFERENCES DISTRIBUTOR(DISTRIBUTOR_ID),
                FOREIGN KEY (CLOTH_ID) REFERENCES CLOTH(CLOTH_ID),
                PRIMARY KEY(CLOTH_ID,DISTRIBUTOR_ID)
)"""
SUPPLY=  """CREATE TABLE SUPPLY (
                CLIENT_ID INT NOT NULL,
                QUANTITY INT NOT NULL,
                CLOTH_ID INT NOT NULL,
				EMPLOYEE_ID INT NOT NULL,
				Date date not null,
                FOREIGN KEY (CLIENT_ID) REFERENCES CLIENT(CLIENT_ID),
                FOREIGN KEY (CLOTH_ID) REFERENCES CLOTH(CLOTH_ID),
				FOREIGN KEY (EMPLOYEE_ID) REFERENCES TRANSPORT_EMPLOYEE(EMP_ID),
                PRIMARY KEY(CLOTH_ID,CLIENT_ID))"""

# table created
cursorObject.execute(CLOTH)
cursorObject.execute(DISTRIBUTOR)
cursorObject.execute(CLIENT)
cursorObject.execute(TRANSPORT_EMPLOYEE)
cursorObject.execute(STOCK)
cursorObject.execute(SUPPLY)