import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",passwd="root",database="userinfo")
mycursor=db.cursor()
#CREATING TABLES

#CREATING USERLOGIN TABLE
#mycursor.execute("CREATE TABLE userlogin (username VARCHAR(20) PRIMARY KEY,password VARCHAR(20))")

#DISPLAYING USERLOGIN TABLE
# mycursor.execute("DESCRIBE userlogin")
#for x in mycursor:
#    print(x)


#CREATING USERPERSONAL TABLE
#fmycursor.execute("CREATE TABLE userpersonal(username VARCHAR(20) PRIMARY KEY,firstname CHAR(20),lastname CHAR(20),gender ENUM('Male', 'Female', 'Transgender', 'Others'),dateofbirth VARCHAR(10),country CHAR(20),state CHAR(20),city CHAR(20),FOREIGN KEY (username) REFERENCES userlogin(username))")

#DISPLAYING USERPERSONAL TABLE
# mycursor.execute("DESCRIBE userpersonal")
#for x in mycursor:
#    print(x)


#CREATING USERCONTACT TABLE
# mycursor.execute("CREATE TABLE usercontact(username VARCHAR(20) PRIMARY KEY,email VARCHAR(40),icc ENUM('+91', '+1', '+44', '+81'),mobileno INT(10),tandc_status ENUM('on', 'off'),FOREIGN KEY (username) REFERENCES userlogin(username))")

#DISPLAYING USER CONTACTT TABLE
#mycursor.execute("DESCRIBE usercontact")
#for x in mycursor:
#    print(x)

#DELETING DATA IN USERLOGIN TABLE
#mycursor.execute("TRUNCATE TABLE userlogin")

#DELETING DATA IN USERLOGIN TABLE
#mycursor.execute("TRUNCATE TABLE userpersonal")

#DELETING DATA IN USERLOGIN TABLE
#mycursor.execute("TRUNCATE TABLE usercontact")

#CHECKING TABLE DATA
#mycursor.execute("SELECT * from userlogin")
#for x in mycursor:
#    print(x)