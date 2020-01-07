
# coding: utf-8

# In[17]:


import sqlite3
from sqlite3 import Error


# In[18]:


#Establising Connection with Sqlite Dabase and creating Database
def SqlConnection():
    try:
        connection = sqlite3.connect('database.db')    #Create database if enetered named database is not present otherwise it points to that database
        return connection                              #return Connection object for accesing connection method for quering
    except Error:
        print(Error)


# In[19]:


# Creating Table
def CreateTable(connection):
    CursorObject = connection.cursor()          #Creating Cursor object for executing the sql query
    CursorObject.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")        #Query for creating Table                   
    connection.commit()


# In[20]:


#Inserting Data
def InsertData(connection):
    CursorObject = connection.cursor()         ##Creating Cursor object for executing the sql query
    CursorObject.execute("INSERT INTO employees VALUES(007, 'Ujjawal Mishra', 24000, 'Software Development', 'Software Developer', '2017-07-08')")       #Inserting data into employee table
    connection.commit()


# In[21]:


#Fetching data from table
def FetchData(connection):
    CursorObject = connection.cursor()         #Creating Cursor object for executing the sql query
    CursorObject.execute('SELECT * FROM employees')     #Query for fetching all data from employee table
    Datas = CursorObject.fetchall()
    for Data in Datas:
        print(Data)


# In[24]:


connection = SqlConnection()     #creating and Establishing connection from database 
CreateTable(connection)         #Creating Table
InsertData(connection)          #inserting data into table
FetchData(connection)           #Fetching and printong data

