Python version : 3.9.5
MongoDB version : 5.0.3

First install the pymongo library using below command

$ pip3 install pymongo

Create a python file and write the below code for importing data from csv to MongoDB WordCountimpExp.py

First connect your python to MongoDB by following below code provided in python file

As we know we can run the above function from the main function by passing mongodb database_name and collection_name

For importing csv file data to the mongodb we can follow the python code 

Pass the proper way of your csv file and name 

We can check in mongodb the mongodb table has been created and data is also store on it


Commands used for the above pictures are
>show dbs
>use StartupExpansion(database_name)
>show collections
>db.count.find().pretty() (where Expansion is collection name)
>db.count.aggregate().pretty() (aggregate will avoid the duplicate entries to be displayed)

Export MongoDB to csv file using python pymongo library

Follow  the below code to transfer the mongoDB data to a csv file 

Csv file will be created as the per given path and name we can read the data of it

Here csv file name is WordCountexported.csv
