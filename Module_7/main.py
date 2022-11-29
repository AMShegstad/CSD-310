# Alexander Shegstad
# 11/29/2022
# Movies_Query

import mysql.connector
from mysql.connector import errorcode

config = {
    "user":"movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
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


# Query 1
cursor = db.cursor()
print(" -- DISPLAYING Studio RECORDS --")
print("________________________________")
cursor.execute("SELECT * from Studio")

# Query 2
cursor = db.cursor()
print("-- DISPLAYING genre RECORDS --")
print("______________________________")
cursor.execute("SELECT * from Genre")

# Query 3
cursor = db.cursor()
print("-- DISPLAYING Short Film RECORDS --")
print("___________________________________")
cursor.execute("SELECT film_name from film WHERE film_runtime < 120")

# Query 4
cursor = db.cursor()
print("-- DISPLAYING Director RECORDS in Order --")
print("__________________________________________")
cursor.execute("SELECT film_name from film GROUP BY film_director")
