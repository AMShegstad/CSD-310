
"""
Milestone #2 - At this point, you should have an initial ERD and a set of business rules. Take another look at the ERD,
add as many details as needed, including attributes for each table, make any revisions as needed. Once you have your
tables in finalized state, write the Python script to create the tables in MySQL, and populate each with at least 6
records (fewer if noted in the case study, for example only three suppliers noted at Bacchus Winery). Write a python
script that displays the data in each table, and take a screenshot of the results of the script that displays the data
in each table. The deliverables this week are: The deliverables this week are: The Python script(s) and a Word document
that has your group name at the top, members of the team, revised ERD, and screenshot(s) of the data displayed from your
tables.
"""

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "Iheartme07!",
    "host": "127.0.0.1",
    "port": "3006",
    "database": "Bacchus_Winery",
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


# Adding Tables to the Bacchus_Winery Database
cursor.execute("CREATE TABLE suppliers (supplier_ID int,supplier_name varchar(20))")

cursor.execute("CREATE TABLE supplies (supplier_ID int, supply_name varChar(30))")

cursor.execute("CREATE TABLE distributors (distributor_ID int, distributor_name varChar(30), distributor_address varChar(30), distributor_since varChar(4))")

cursor.execute("Create table products(wine_type varChar(20), lot_number int, bottle_volume int, product_number int, case_number int)")

cursor.execute("Create table departments(department_name varChar(20))")

cursor.execute("Create table employees(Department_name varChar(20), employee_count int)")

cursor.execute("Create table grapes(grape_color varChar(30), wine_type1 varChar(30), wine_type2 varChar(30))")

cursor.execute("Create table wines(label_name varChar(30), wine_type varChar(30))")

cursor.execute("Create table orders(order_ID int, customer_ID int , tracking_ID varChar(20))")

cursor.execute("Create table tracking_numbers(tracking_ID varChar(20), shipping_address varChar(20))")


# Using a ton of scripts to insert data into the tables.

# Adding entries to Suppliers table
cursor.execute("INSERT INTO suppliers VALUES (1, 'Dunder_Mifflin')")
cursor.execute("INSERT INTO suppliers (supplier_ID, supplier_name) VALUES (2, 'Food_Prep_Depot')")
cursor.execute("INSERT INTO suppliers (supplier_ID, supplier_name) VALUES (3, 'Johnson_Supplies')")


# Adding entries to Supplies table
cursor.execute("INSERT INTO supplies (supplier_ID, supply_name) VALUES (4, 'boxes')")
cursor.execute("INSERT INTO supplies (supplier_ID, supply_name) VALUES (5, 'labels')")
cursor.execute("INSERT INTO supplies (supplier_ID, supply_name) VALUES (6, 'bottles')")
cursor.execute("INSERT INTO supplies (supplier_ID, supply_name) VALUES(0002, 'corks')")
cursor.execute("INSERT INTO supplies (supplier_ID, supply_name) VALUES (0003, 'vats')")
cursor.execute("INSERT INTO supplies (supplier_ID, supply_name) VALUES (0003, 'tubing')")


# Adding entries to the Distributors tables
cursor.execute("INSERT INTO Distributors (distributor_ID, distributor_name, distributor_address, distributor_since) "
               "VALUES (1001, 'Wine_World', '123 Johnson Street', 2020)")
cursor.execute("INSERT INTO Distributors (distributor_ID, distributor_name, distributor_address, distributor_since) "
               "VALUES (1002, 'ABC_Spirits', '10 Roosevelt Rd', 2019)")
cursor.execute("INSERT INTO Distributors (distributor_ID, distributor_name, distributor_address, distributor_since) "
               "VALUES (1003, 'WalMart', '34 Main St', 2016)")
cursor.execute("INSERT INTO Distributors (distributor_ID, distributor_name, distributor_address, distributor_since) "
               "VALUES (1004, 'Thats The Spirit', '9732 Belvedere dr', 2012)")
cursor.execute("INSERT INTO Distributors (distributor_ID, distributor_name, distributor_address, distributor_since) "
               "VALUES (1005, 'Canadian_Fine_Liquors', '25 Quebec Way', 2021)")
cursor.execute("INSERT INTO Distributors (distributor_ID, distributor_name, distributor_address, distributor_since) "
               "VALUES (1006, 'Wine_N_Dine', '534 75th Ave', 2016)")


# Adding entries into the products table
cursor.execute("INSERT INTO products (wine_type, lot_number, bottle_volume, product_number,case_number) "
               "VALUES ('blank', 143, 40, 101, 2341)")
cursor.execute("INSERT INTO products (wine_type, lot_number, bottle_volume, product_number,case_number) "
               "VALUES ('blank', 232, 40, 102, 5340)")
cursor.execute("INSERT INTO products (wine_type, lot_number, bottle_volume, product_number,case_number) "
               "VALUES ('blank', 131, 40, 103, 1234)")
cursor.execute("INSERT INTO products (wine_type, lot_number, bottle_volume, product_number,case_number) "
               "VALUES ('blank', 412, 40, 104, 1213)")
cursor.execute("INSERT INTO products (wine_type, lot_number, bottle_volume, product_number,case_number) "
               "VALUES ('blank', 035, 20, 105, 1123)")
cursor.execute("INSERT INTO products (wine_type, lot_number, bottle_volume, product_number,case_number) "
               "VALUES ('blank', 351, 20, 106, 1242)")


# Adding entries into the Department table
cursor.execute("INSERT INTO departments (department_name) VALUES ('distribution')")
cursor.execute("INSERT INTO departments (department_name) VALUES ('payroll')")
cursor.execute("INSERT INTO departments (department_name) VALUES ('production')")
cursor.execute("INSERT INTO departments (department_name) VALUES ('marketing')")


# Adding entries into the Employees table
cursor.execute("INSERT INTO employees (department_name, employee_count) VALUES('finances_and_Payroll', 1)")
cursor.execute("INSERT INTO employees (department_name, employee_count) VALUES('marketing', 2)")
cursor.execute("INSERT INTO employees (department_name, employee_count) VALUES('Production', 21)")
cursor.execute("INSERT INTO employees (department_name, employee_count) VALUES('distribution', 1)")


# Adding entries into te Orders table
cursor.execute("INSERT INTO orders (order_ID, customer_ID, tracking_ID) VALUES(143, 2001, '1432001')")
cursor.execute("INSERT INTO orders (order_ID, customer_ID, tracking_ID) VALUES(165, 2002, '1652002')")
cursor.execute("INSERT INTO orders (order_ID, customer_ID, tracking_ID) VALUES(134, 2003, '1342003')")
cursor.execute("INSERT INTO orders (order_ID, customer_ID, tracking_ID) VALUES(213, 2004, '2132004')")
cursor.execute("INSERT INTO orders (order_ID, customer_ID, tracking_ID) VALUES(142, 2005, '1422005')")
cursor.execute("INSERT INTO orders (order_ID, customer_ID, tracking_ID) VALUES(178, 2006, '1782006')")


# Adding entries into the Tracking_Number table
cursor.execute("INSERT INTO tracking_numbers (tracking_ID, shipping_address) VALUES('1432001', '12 Main st')")
cursor.execute("INSERT INTO tracking_numbers (tracking_ID, shipping_address) VALUES('1652002', '423 Roberts Ridge')")
cursor.execute("INSERT INTO tracking_numbers (tracking_ID, shipping_address) VALUES('1342004', '46 Edmonton Place')")
cursor.execute("INSERT INTO tracking_numbers (tracking_ID, shipping_address) VALUES('2132004', '2022 Colorado Ave')")
cursor.execute("INSERT INTO tracking_numbers (tracking_ID, shipping_address) VALUES('1422005', '1597 Airport Rd')")
cursor.execute("INSERT INTO tracking_numbers (tracking_ID, shipping_address) VALUES('1782006', '6 Pennsylvania Ave')")


# Adding entries into the Grapes table
cursor.execute("INSERT INTO grapes (grape_color, wine_type1, wine_type2) VALUES('red', 'merlot', null)")
cursor.execute("INSERT INTO grapes (grape_color, wine_type1, wine_type2) VALUES('red', 'cabernet', null)")
cursor.execute("INSERT INTO grapes (grape_color, wine_type1, wine_type2) VALUES('white', 'chablis', 'chardonnay')")


# Adding entries into the Wines table
cursor.execute("INSERT INTO wines (label_name, wine_type) VALUES('Bacchus Winery Merlot', 'Merlot') ")
cursor.execute("INSERT INTO wines (label_name, wine_type) VALUES('Bacchus Winery Cabernet', 'Cabernet')")
cursor.execute("INSERT INTO wines (label_name, wine_type) VALUES('Bacchus Winery Chablis', 'Chablis')")
cursor.execute("INSERT INTO wines (label_name, wine_type) VALUES('Bacchus Winery Chardonnay', 'Chardonnay')")


# Displaying each table, one by one

# Suppliers table
print("---------------------------")
print("Displaying Supplier Records")
print("---------------------------")
cursor.execute("SELECT * from suppliers")
suppliers = cursor.fetchall()
print("{}\n{}\n{}".format(suppliers[0], suppliers[1], suppliers[2]))


# Supplies table
print("---------------------------")
print("Displaying Supplies Records")
print("---------------------------")
cursor.execute("SELECT * from supplies")
supplies = cursor.fetchall()
print("{}\n{}\n{}\n{}\n{}\n{},".format(supplies[0], supplies[1], supplies[2], supplies[3], supplies[4], supplies[5]))
print()

#
print("------------------------------")
print("Displaying Distributor Records")
print("------------------------------")
cursor.execute("SELECT * from distributors")
distributors = cursor.fetchall()
print("{}\n{}\n{}\n".format(distributors[0], distributors[1], distributors[2], distributors[3]))


print("---------------------------")
print("Displaying Products Records")
print("---------------------------")
cursor.execute("SELECT * from products")
products = cursor.fetchall()
print("{}\n{}\n{}\n{}\n{}".format(products[0], products[1], products[2], products[3], products[4]))

print("---------------------------")
print("Displaying Departments Records")
print("---------------------------")
cursor.execute("SELECT * from departments")
departments = cursor.fetchall()
print("{}".format(suppliers[0]))
print()

print("---------------------------")
print("Displaying Employees Records")
print("---------------------------")
cursor.execute("SELECT * from employees")
employees = cursor.fetchall()
print("{}\n{}".format(employees[0], employees[1]))
print()

print("---------------------------")
print("Displaying Grapes Records")
print("---------------------------")
cursor.execute("SELECT * from grapes")
grapes = cursor.fetchall()
print("{}\n{}\n{}".format(grapes[0], grapes[1], grapes[2]))
print()

print("---------------------------")
print("Displaying Wine Records")
print("---------------------------")
cursor.execute("SELECT * from wines")
wines = cursor.fetchall()
print("{}\n{}".format(wines[0], wines[1]))
print()


print("---------------------------")
print("Displaying Orders Records")
print("---------------------------")
cursor.execute("SELECT * from orders")
orders = cursor.fetchall()
print("{}\n{}\n{}".format(orders[0], orders[1], orders[2]))
print()

print("-----------------------------------")
print("Displaying Tracking Numbers Records")
print("-----------------------------------")
cursor.execute("SELECT * from tracking_numbers")
tracking_numbers = cursor.fetchall()
print("{}\n{}".format(tracking_numbers[0], tracking_numbers[1]))
print()