import sqlite3

##connect to sqllite
connection=sqlite3.connect("student.db")
## create a cursor object to create update delete retrieve 
cursor=connection.cursor()
##create table
table_info="""create table student 
(name varchar(25),class varchar(25),
section varchar(25),marks int
)
"""

cursor.execute(table_info)
## insert some more record
cursor.execute("insert into student values('ajay','web dev','A','90')")
cursor.execute("insert into student values('raj','data science','B','80')")
cursor.execute("insert into student values('salman','dev ops','c','90')")
cursor.execute("insert into student values('vipin','ML','A','72')")
cursor.execute("insert into student values('sanjay','APP dev','D','85')")
  
  ##display all the record
print("The inserted records are")
data=cursor.execute("select * from student")

for row in data:
    print(row)
##    close the connection
connection.commit()
connection.close()  