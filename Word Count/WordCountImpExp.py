
"""
* @Author: Mohammad Fatha
* @Date: 2021-11-17 2:15
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-17-16 2:30
* @Title: : Python program to import and export Word count ouput data from/to MongoDB using pymongo library
"""
from logging import log
import pymongo
from pymongo import MongoClient
import pandas as pd
import json
from LogHandler import logger
class MongoDB():

    def __init__(self, dBName=None , collectionName=None):

        """
        Description: 
            This function is used to establish the connection between python and MongoDB
        """
        try:
            self.dBName = dBName
            self.collectionName = collectionName

            self.client = MongoClient("localhost", 27017,maxPoolSize=50)
            self.DB = self.client[self.dBName]
            self.collection = self.DB[self.collectionName]
            logger.info("connection has been established")
        except Exception as e:
            logger.error(e)

    def import_data_into_db (self, path=None):
        """
        Description: 
            This function is used import data to MongoDB from csv fil 
        """
        try:
            df = pd.read_csv(path)
            data = df.to_dict("records")

            self.collection.insert_many(data, ordered=False)
            logger.info("All the data has been imported to Database from csv file")
        except Exception as e:
            logger.error(e)
    
    def export_data_to_db(self):
        """
        Description: 
            This function is used to export data from MongoDB to csv file
        """
        try:
            cursor = self.collection.find()
            df = pd.DataFrame(list(cursor))
            df.to_csv("MongoDBImportExport/WordCountexpcsv.csv")
            logger.info("All the data has been exported from Database to csv file")
        except Exception as e:
            logger.error(e)


if __name__ == "__main__":
    mongodb = MongoDB(dBName='WordCount', collectionName='count')
    mongodb.import_data_into_db(path='/home/fatha/Documents/MongoDB/Word Count/Word_Count.csv')
    mongodb.export_data_to_db()
