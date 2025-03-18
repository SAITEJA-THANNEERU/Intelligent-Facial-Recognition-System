import pymysql

# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="5959",
#     database="Users"
# )
# print(mydb)

# mycursor=mydb.cursor()
# mycursor.execute("CREATE DATABASE Users") #Students has replaced with Users


mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="5959",
    database="User"
)
mycursor=mydb.cursor()  #table stu_table
#mycursor.execute("CREATE DATABASE Users") #Students has replaced with Users
mycursor.execute("CREATE TABLE users(id int auto_increment primary key, name varchar(50),age int)")