Python version : 3.9.5

MongoDB version : 5.0.3

Import and Export operation using python pymongo library in MongoDB

Import csv file to MongoDB using python pymongo library

First install the pymongo library using below command

$ pip3 install pymongo

Create a python file and write the below code for importing data from csv to MongoDB mongoimportexport.py

First connect your python to MongoDB by following below code

As we know we can run the above function from the main function by passing mongodb database_name and collection_name

For importing csv file data to the mongodb we can follow the below code 

Pass the proper way of your csv file and name 

We can check in mongodb the mongodb table has been created and data is also store on it

Commands used for the check in MongoDB shell

>show dbs
>use StartupExpansion(database_name)
>show collections
>db.Expansion.find().pretty() (where Expansion is collection name)

Export MongoDB to csv file using python pymongo library

Follow  the below code from provided python file to transfer the mongoDB data to a csv file 

Csv file will be created as the per given path and name we can read the data of it 
