import mysql.connector
#
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root_123_456_789",
  database="project"
)
#
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE project")
mycursor.execute("CREATE TABLE mydatabase (user_name VARCHAR(255),email VARCHAR(255) UNIQUE,password VARCHAR(255) UNIQUE,ssn INT UNIQUE,address VARCHAR(255),id INT UNIQUE,PRIMARY KEY (ssn) )")
# for x in mycursor:
#       print(x)