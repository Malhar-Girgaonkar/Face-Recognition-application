import mysql.connector

def create_tables(cursor):
    # CREATING USERLOGIN TABLE
    cursor.execute("CREATE TABLE IF NOT EXISTS userlogin (username VARCHAR(20) PRIMARY KEY,password VARCHAR(20))")

    # CREATING USERPERSONAL TABLE
    cursor.execute("CREATE TABLE IF NOT EXISTS userpersonal(username VARCHAR(20) PRIMARY KEY,firstname CHAR(20),lastname CHAR(20),gender ENUM('Male', 'Female', 'Transgender', 'Others'),dateofbirth VARCHAR(10),country CHAR(20),state CHAR(20),city CHAR(20),FOREIGN KEY (username) REFERENCES userlogin(username))")

    # CREATING USERCONTACT TABLE
    cursor.execute("CREATE TABLE IF NOT EXISTS usercontact(username VARCHAR(20) PRIMARY KEY,email VARCHAR(40),icc ENUM('+91', '+1', '+44', '+81'),mobileno INT(10),tandc_status ENUM('on', 'off'),FOREIGN KEY (username) REFERENCES userlogin(username))")

def main():
    host = "localhost"
    user = "root"
    password = "root"
    database_name = "userinfo"

    try:
        db = mysql.connector.connect(host=host, user=user, passwd=password)
        cursor = db.cursor()

        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        cursor.execute(f"USE {database_name}")
        
        create_tables(cursor)
        db.commit()
        print("Database and tables created successfully.")

    except mysql.connector.Error as error:
        print("Error:", error)

    finally:
        if 'db' in locals() and db.is_connected():
            cursor.close()
            db.close()

if __name__ == "__main__":
    main()
