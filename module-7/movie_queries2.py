

# Somsak Bounchareune
# November 25, 2023
# Assignment 7.2


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

    print("\nDatabase user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                     config["database"]))

    cursor = db.cursor()

    # Query 1: Select all fields from the studio table
    cursor.execute("SELECT * FROM studio")
    studio_data = cursor.fetchall()

    print("\nQuery 1: All fields from the studio table")
    for row in studio_data:
        print(row)

    print("\n---------------------------------\n")

    # Query 2: Select all fields from the genre table
    cursor.execute("SELECT * FROM genre")
    genre_data = cursor.fetchall()

    print("Query 2: All fields from the genre table")
    for row in genre_data:
        print(row)

    print("\n---------------------------------\n")

    # Query 3: Select movie names with a run time of less than two hours
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    movies_less_than_two_hours = cursor.fetchall()

    print("Query 3: Movie names and runtimes with a run time of less than two hours")
    for row in movies_less_than_two_hours:
        print(f"Film: {row[0]}, Runtime: {row[1]} minutes")

    print("\n---------------------------------\n")

    # Query 4: Get a list of film names and directors ordered by director
    cursor.execute("SELECT film_name, film_director, film_runtime FROM film ORDER BY film_director")
    movies_directors_ordered = cursor.fetchall()

    print("Query 4: Film names and directors by director")
    for row in movies_directors_ordered:
        print(f"Film: {row[0]}, Director: {row[1]}")

    cursor.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)
finally:
    db.close()

# I had to rewrite this. The previous code I thought I uploaded was blank. Was having challenges with Git
# And did not confirm it was successfully uploaded. 

