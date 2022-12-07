"""
Alexander Shegstad
Movies: Updates and Deletes
11/29/2022
"""

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "Iheartme07!",
    "host": "127.0.0.1",
    "port": "3006",
    "database": "movies",
    "raise_on_warnings": True
}
db = mysql.connector.connect(**config)

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MYSQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
    db.close()

db = mysql.connector.connect(**config)
cursor = db.cursor()

# method to execute an inner join on all tables,
# iterate over the dataset and output the results to the terminal window


def show_films(cursor, title):

    # Inner join query (Think of x=y as the center of the venn diagram between x and y)
    cursor.execute("SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")

    # get the results from the cursor object
    films = cursor.fetchall()

    print("\n == {} ==".format(title))

    # iterate over the film data set and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))


# The first use of the show_films() method
show_films(cursor, "Displaying Films")


cursor.execute("INSERT INTO films (film_name, genre, director, releaseDate)")