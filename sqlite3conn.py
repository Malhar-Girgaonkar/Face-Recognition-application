import sqlite3

# Establish a connection to the SQLite database
connection = sqlite3.connect("userinfo.db")
cursor = connection.cursor()

# CREATING TABLES

# CREATING USERLOGIN TABLE
#cursor.execute("CREATE TABLE userlogin (username TEXT PRIMARY KEY, password TEXT)")

# DISPLAYING USERLOGIN TABLE
#cursor.execute("PRAGMA table_info(userlogin)")
#for x in cursor:
#    print(x)

# CREATING USERPERSONAL TABLE
#cursor.execute("CREATE TABLE userpersonal (username TEXT PRIMARY KEY, firstname TEXT, lastname TEXT, gender TEXT, dateofbirth TEXT, country TEXT, state TEXT, city TEXT, FOREIGN KEY (username) REFERENCES userlogin(username))")

# DISPLAYING USERPERSONAL TABLE
#cursor.execute("PRAGMA table_info(userpersonal)")
#for x in cursor:
#    print(x)

# CREATING USERCONTACT TABLE
#cursor.execute("CREATE TABLE usercontact (username TEXT PRIMARY KEY, email TEXT, icc TEXT, mobileno TEXT, tandc_status TEXT, FOREIGN KEY (username) REFERENCES userlogin(username))")

# DISPLAYING USERCONTACT TABLE
#cursor.execute("PRAGMA table_info(usercontact)")
#for x in cursor:
#    print(x)

# DELETING DATA IN USERLOGIN TABLE
#cursor.execute("DELETE FROM userlogin")

# DELETING DATA IN USERPERSONAL TABLE
#cursor.execute("DELETE FROM userpersonal")

# DELETING DATA IN USERCONTACT TABLE
#cursor.execute("DELETE FROM usercontact")

# CHECKING TABLE DATA
cursor.execute("SELECT * FROM userlogin")
for x in cursor:
    print(x)

# Commit the changes and close the connection
#connection.commit()
connection.close()
