# Imports
import pandas as pd
from pymongo import MongoClient


data = pd.read_csv('./deaths.csv')


def create_db():
    CONNECTION_STRING = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.8.0"
    client =  MongoClient(CONNECTION_STRING)
    return client['dbprojet']


mydb = create_db()

myCollection = mydb['cida']

data.reset_index(inplace=False)

data_dict = data.to_dict("records")

def intoMontgo(myCollection):
    myCollection.insert_many(data_dict)

intoMongo = intoMontgo(myCollection)