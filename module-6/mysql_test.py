

# Somsak Bounchareune
# November 19, 2023
# Assignment 6.2


import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "Pancakes$1Go",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True

}
try:
    db = mysql.connector.connect(**config)

    print("\nDatabase user {} connect to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\nPress any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)
finally:
    db.close()
