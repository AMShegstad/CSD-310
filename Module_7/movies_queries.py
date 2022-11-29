# Alexander Shegstad
# 11/29/2022
# Movies_Query

"""
Create a new file under the module_7 directory and name it movies_queries.py.
Write the code to connect to your MySQL movies database. Refer to the previous assignment for code structure.
You can basically copy/paste the code we used in the previous assignment, assuming you were able to get it to work.
Write four queries, in one Python file.The output from your queries should match the example below, including descriptions of output and format.

The first and second query is to select all the fields for the studio and genre tables.

The third query is to select the movie names for those movies that have a run time of less than two hours.

The fourth query is to get a list of film names, and directors grouped by director.

Run the script and take a screenshot of the results.

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

# Query 1
print("________________________________")
print(" -- DISPLAYING Studio RECORDS --")
print("________________________________")
cursor.execute("SELECT * from Studio")
studios = cursor.fetchall()
for studio in studios:
    print("Studio ID#: {}\nStudio Name: {}".format(studio[0], studio[1]))
    print()

# Query 2
print("______________________________")
print("-- DISPLAYING genre RECORDS --")
print("______________________________")
cursor.execute("SELECT * from Genre")
genres = cursor.fetchall()
for genre in genres:
    print("Genre ID#: {}\nGenre Name: {}".format(genre[0], genre[1]))
    print()

# Query 3
print("___________________________________")
print("-- DISPLAYING Short Film RECORDS --")
print("___________________________________")
cursor.execute("SELECT film_name, film_runtime from film")
# I tried to add the time exclusion to the above statement, but it wasn't working.'
shortFilms = cursor.fetchall()
for shortFilm in shortFilms:
    if shortFilm[1] < 120:
        print("Film Title: {}\nRuntime: {} minutes".format(shortFilm[0], shortFilm[1]))
        print()

# Query 4
print("__________________________________________")
print("-- DISPLAYING Director RECORDS in Order --")
print("__________________________________________")
cursor.execute("SELECT film_name, film_director from film GROUP BY film_director")
directors = cursor.fetchall()
for director in directors:
    print("Film Title: {}\nDirector: {}".format(director[0], director[1]))
    print()