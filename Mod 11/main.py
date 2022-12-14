"""
Team "TarDisFlo"is
Alexander Shegstad
Sabrina Taucat
Luis Padilla
Tiffany Suratt

Milestone #3 – Read through the case study again, and determine what information, retrieved from the tables
(basically a report), will be helpful in making the business decisions listed in the case study. There should
be a minimum of three reports.  Provide a description of the report, write the Python script to create the
report, and take a screenshot of each report (result of query). The deliverables this week are: The Python
script(s) and a Word document that has your group name at the top, members of the team, description of the
reports, and screenshot(s) of the results of running the queries.
"""

import mysql.connector
from mysql.connector import errorcode
from tabulate import tabulate

config = {
    "user": "root",
    "password": "Iheartme07!",
    "host": "127.0.0.1",
    "port": "3006",
    "database": "bacchus_winery",
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

"""
Employee time. During the last four quarters, how many hours did each employee work?

This report will take information from both the employees and department tables to show every employee, how much they 
have worked through each quarter, and even which department they are in.
"""
cursor.execute("SELECT employee_ID, first_name, last_name, department_name, hoursWorked_lastQtr, hoursWorked_2QtrPrev," 
               "hoursWorked_3QtrPrev, hoursWorked_4QtrPrev FROM employees INNER JOIN departments on "
               "departments.department_ID=employees.department_ID")

# Assign results to "EmployeePay"
employeePay = cursor.fetchall()

# Calculating the total yearly hours worked for each employee.
q4_hours = employeePay[4]
q3_hours = employeePay[5]
q2_hours = employeePay[6]
q1_hours = employeePay[7]

# Make it one number
yearlyHours = str(q4_hours + q3_hours + q2_hours + q1_hours)

# Display the data neatly
print(tabulate(employeePay, headers=["Employee ID#", "First Name", "Last Name","Department", "Q4 Hours", "Q3 Hours",
                                     "Q2 Hours", "Q1 Hours"]))
print("\n\n")

"""
# The wine distribution, are all wines selling as they thought? Is one wine not selling?

This report, similarly to the employee pay report, I have the data divided up into quarters, allowing the user to view 
trends as opposed to the year-end information.
"""
# SQL statement
cursor.execute("SELECT wine_type, sold_lastQtr, sold_2QtrPrev, sold_3QtrPrev, sold_4QtrPrev FROM wines")
# Assign to wines
wines = cursor.fetchall()
# adding numbers to variables to more easily handle data.
for wine in wines:
    q4_sales = wine[1]
    q3_sales = wine[2]
    q2_sales = wine[3]
    q1_sales = wine[4]
    yearlyUnitsSold = str(q4_sales + q3_sales + q2_sales + q1_sales)

    salesData = [wine[0], yearlyUnitsSold]

print(tabulate(wines, headers=["Wine", "Sold Last Quarter", "Sold 2 Quarters Prev", "Sold 3 Quarters Prev",
                               "Sold 4 Quarters Prev"]))

print("\n\n")
"""
Which distributor carries which wine? This report takes information from distributor table and shows who carries 
which wine.
"""
cursor.execute("SELECT distributor_name, wine_type1, wine_type2, wine_type3, wine_type4 FROM distributors")

distributors = cursor.fetchall()

print(tabulate(distributors, headers=["Distributor", "Wine carried", "Wine carried", "Wine carried", "Wine carried"]))
print("\n\n")

"""
# Are all suppliers delivering on time? Is there a large gap between expected delivery and actual delivery?
"""
# SQL Statement with inner join to get the supplier name which is located on a different table.
cursor.execute("SELECT order_ID, supplier_name, order_date, expected_date, delivery_date FROM orders INNER JOIN "
               "suppliers ON suppliers.supplier_ID = orders.supplier_ID")
# Assign results to supplies
suppliers = cursor.fetchall()

print(tabulate(suppliers, headers=["Order ID#", "Supplier", "Date Ordered", "Promised By", "Delivered on"]))
