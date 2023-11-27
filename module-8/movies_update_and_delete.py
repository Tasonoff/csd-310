# Somsak Bounchareune
# November 26, 2023
# Assignment 8.2


import mysql.connector

# Function to display films
def show_films(cursor, title):
    # method to execute an inner join on all tables,
    # iterate over the dataset and output the results to the terminal window

    # inner join query with corrected SQL syntax
    cursor.execute(
        "SELECT film_name AS Name, film_director AS Director, genre_name AS Genre, studio_name AS 'Studio Name' FROM film INNER JOIN genre ON film.genre_id = genre.genre_id INNER JOIN studio ON film.studio_id = studio.studio_id")

    # get the results from the cursor object
    films = cursor.fetchall()

    print("\n -- {} --".format(title))  # Added a closing parenthesis

    # iterate over the film data set and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))  # Changed the format placeholders to match the columns

try:
    config = {
        "user": "root",
        "password": "Pancakes$1Go",
        "host": "127.0.0.1",
        "database": "movies",
        "raise_on_warnings": True
    }

    # Establish a connection to the database
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    # Display films before any modifications
    show_films(cursor, "DISPLAYING FILMS")

    # Replace studio_id and genre_id with appropriate IDs for insertion and update
    studio_id = 1  # Replace with the appropriate studio ID
    genre_id = 1   # Replace with the appropriate genre ID

    # Insert a new record into the film table
    cursor.execute(
        "INSERT INTO film(film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES (%s, %s, %s, %s, %s, %s)",
        ("28 Days Later", "2002", "113", "Danny Boyle", studio_id, genre_id))
    db.commit()  # Commit the transaction

    # Display films after inserting a new record
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # Update 'Alien' to a Horror film
    horror_genre_id = 1  # Assuming the horror genre ID is 1 (replace with the actual ID)
    cursor.execute("UPDATE film SET genre_id = %s WHERE film_name = %s", (horror_genre_id, "Alien"))
    db.commit()  # Commit the transaction

    # Display films after updating 'Alien' to a Horror film
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")

    # Delete the movie 'Gladiator'
    cursor.execute("DELETE FROM film WHERE film_name = %s", ("Gladiator",))
    db.commit()  # Commit the transaction

    # Display films after deleting 'Gladiator'
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

except mysql.connector.Error as error:
    print("Error: {}".format(error))

finally:
    # Close cursor and database connection
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'db' in locals() and db.is_connected():
        db.close()
