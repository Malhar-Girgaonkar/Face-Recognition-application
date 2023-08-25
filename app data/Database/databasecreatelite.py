import sqlite3
import os

def create_tables(cursor):
    # CREATING USERLOGIN TABLE
    cursor.execute('''CREATE TABLE IF NOT EXISTS userlogin (
                        username TEXT PRIMARY KEY,
                        password TEXT)''')

    # CREATING USERPERSONAL TABLE
    cursor.execute('''CREATE TABLE IF NOT EXISTS userpersonal(
                        username TEXT PRIMARY KEY,
                        firstname TEXT,
                        lastname TEXT,
                        gender TEXT,
                        dateofbirth TEXT,
                        country TEXT,
                        state TEXT,
                        city TEXT,
                        FOREIGN KEY (username) REFERENCES userlogin(username))''')

    # CREATING USERCONTACT TABLE
    cursor.execute('''CREATE TABLE IF NOT EXISTS usercontact(
                        username TEXT PRIMARY KEY,
                        email TEXT,
                        icc TEXT,
                        mobileno INTEGER,
                        tandc_status TEXT,
                        FOREIGN KEY (username) REFERENCES userlogin(username))''')

def main():
    database_file = "userinfo.db"

    # Check if the database file exists
    if not os.path.exists(database_file):
        try:
            db = sqlite3.connect(database_file)
            cursor = db.cursor()

            create_tables(cursor)
            db.commit()
            print("Database and tables created successfully.")

        except sqlite3.Error as error:
            print("Error:", error)

        finally:
            if db:
                cursor.close()
                db.close()
    else:
        print("Database file already exists.")

if __name__ == "__main__":
    main()