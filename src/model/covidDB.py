import ssl

import pymongo
from pymongo import MongoClient
__doc__ = """
covidDB - accesses and manipulates data from the model

This class connects to a MongoDB cluster.
The serverless cloud infrastructure is set up using MongoDB Atlas
=====================================================================
Main Features
-------------
List of main features of controller:
  - Load records into the database
  - CRUD operations on the database
  - Delete everything from the database
--------------
@Author: Anton Hrytsyk   
"""


# client = MongoClient("mongodb+srv://antonh:antonh@cluster0.keboi.mongodb.net/<dbname>?retryWrites=true&w=majority")
# db = client.cluster["InternationalCovid19Cases"]
# collection = db["records"]
class CovidDB:
    # Default initialization
    client = None
    db = None
    collection = None

    def __init__(self, client, cluster, collection):
        """
        client: uri to a mongoDB cluster
        cluster: name of the cluster
        collection: name of the collection
        """
        self.client = MongoClient(client, ssl_cert_reqs=ssl.CERT_NONE)
        self.db = self.client.cluster[cluster]
        self.collection = self.db[collection]

    def insert_single_record(self, _id, id, date, cases, deaths, name_fr, name_en):
        """ Insert a new rercord
                        Parameters:
                        argument1 (string): _id of the new record
                        argument2 (string): id of the new record
                        argument3 (string): date of the new record
                        argument4 (string): cases of the new record
                        argument5 (string): deaths of the new record
                        argument6 (string): name_fr of the new record
                        argument7 (string): name_en of the new record
                """
        self.collection.insert_one({"_id": int(_id), "id": id, "date": date,
                                    "cases": float(cases), "deaths": float(deaths), "name_fr": name_fr, "name_en": name_en})

    def delete_single_record(self, field, value):
        """
        Delete a record
        """
        self.collection.delete_one({field: value})

    def delete_everything(self):
        """
        Delete everything
        """
        self.collection.delete_many({})

    def search_records(self, field, value):
        """"
        Search record(s)
        """
        return self.collection.find({field: value})

    def find_one_record(self, field, val):
        """
        find one record
        """
        return self.collection.find_one({field: val})

    def update_record(self, record_id, field, new_value):
        """
        Update record
        """
        self.collection.update_one({"_id": record_id}, {"$set": {field: new_value}})

    def load_records(self, records_json):
        """
        load record
        """
        self.collection.insert_many(records_json)

    def select_all_records(self):
        """
        select all records
        """
        return self.collection.find({})

    def search_and(self, field1, param1, field2, param2):
        """
        Search records on two parameters with AND
        """
        return self.collection.find({"$and":[{field1:param1}, {field2:param2}]})

    def search_or(self, field1, param1, field2, param2):
        """
        Search records on two parameters with OR
        """
        return self.collection.find({"$or":[{field1:param1}, {field2:param2}]})
