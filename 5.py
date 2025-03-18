# import pymysql 

# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="5959",
    
# )

# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE Authorized_user")
# mydb.commit()

# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="5959",
#     database="Authorized_user"
# ) 

# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE User(id int primary key, Name varchar(50), Age int, Address varchar(50))")
# mydb.commit()
# print("sucess")

import pymysql

try:
    # Connect to the MySQL server
    mydb = pymysql.connect(
        host="localhost",
        user="root",
        password="5959"
    )

    mycursor = mydb.cursor()

    # Create database
    mycursor.execute("CREATE DATABASE IF NOT EXISTS Authorized_user")
    mydb.commit()
    print("Database created successfully")

    # Connect to the newly created database
    mydb = pymysql.connect(
        host="localhost",
        user="root",
        password="5959",
        database="Authorized_user"
    )

    mycursor = mydb.cursor()

    # Create table
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS User (
            id INT PRIMARY KEY,
            Name VARCHAR(50),
            Age INT,
            Address VARCHAR(50)
        )
    """)
    mydb.commit()
    print("Table created successfully")

except pymysql.Error as e:
    print(f"Error occurred: {e}")

finally:
    if mydb:
        mydb.close()
