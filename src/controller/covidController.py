import pathlib
import threading
import concurrent.futures

import pymongo
import csv
import json
import pandas as pd
from pandas import DataFrame
from pymongo import MongoClient

from model.covidDB import CovidDB
from model.record import Record


class CovidController:
    client_link = "mongodb+srv://antonh:wswwtfsl@cluster0.keboi.mongodb.net/<dbname>?retryWrites=true&w=majority"
    cluster_name = "InternationalCovid19Cases"
    collection_name = "records"

    model = CovidDB(client_link, cluster_name, collection_name)

    @staticmethod
    def load_records():
        """
        Loads records into the database
        """
        CovidController.model.delete_everything()
        data = None
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(pd.read_csv, str(
                pathlib.Path(__file__).parent.parent.absolute()) + '/model/InternationalCovid19Cases.csv')
            data = future.result()

        thread = threading.Thread(target=CovidController.model.load_records, args=(data.to_dict("records"),))
        thread.start()
        thread.join()

    @staticmethod
    def select_all_records():
        return CovidController.model.select_all_records()

    @staticmethod
    def create_record(record):
        CovidController.model.insert_single_record(
            record._id, record.id, record.date,
            record.cases, record.deaths,
            record.name_fr, record.name_en)

    @staticmethod
    def search_record(field, value):
        if field == "_id":
            value = int(value)
        if field == "cases" or field == "deaths":
            value = float(value)
        cursor = CovidController.model.search_records(field, value)
        return cursor

    @staticmethod
    def find_one_record(field, val):
        if field == "_id" :
            val = int(val)
        c = CovidController.model.find_one_record(field, val)
        return c

    @staticmethod
    def delete_record(field, value):
        CovidController.model.delete_single_record(field, value)

    @staticmethod
    def update_record(record_id, field, value):
        CovidController.model.update_record(int(record_id), field, value)

    @staticmethod
    def to_df(_id, id, date, cases, deaths, name_fr, name_en):
        """ Constructs a new dataframe object that can be used by pandas to write to csv
                Parameters:
                argument1 (string): _id of the new record
                argument2 (string): id of the new record
                argument3 (string): date of the new record
                argument4 (string): cases of the new record
                argument5 (string): deaths of the new record
                argument6 (string): name_fr of the new record
                argument7 (string): name_en of the new record
        """
        data = {"_id": [_id],
                "id": [id],
                "date": [date],
                "cases": [cases],
                "deaths": [deaths],
                "name_fr": [name_fr],
                "name_en": [name_en]
                }
        return pd.DataFrame(data)

    @staticmethod
    def load_into_records(dataframe):
        """ Iterates over the data and loads it into a list of Record objects.
        Parameters:
            dataframe (pandas.core.frame.DataFrame): data from the csv file

        Returns:
            list: A list of Record objects
        """
        records = list()
        for i, j in dataframe.iterrows():
            records.append(
                Record(j['_id'], j['id'], j['date'], j['cases'], j['deaths'], j['name_fr'], j['name_en']))
        return records

    @staticmethod
    def get_loaded_records():
        # Anton Hrytsyk 040938383
        """
        Get dataframe object from the database
        """
        list_f = list(CovidController.model.select_all_records())
        return DataFrame(list_f)

    @staticmethod
    def insert_record(_id, id, date, cases, deaths, name_fr, name_en):
        CovidController.model.insert_single_record(int(_id), id, date, cases, deaths, name_fr, name_en)

    @staticmethod
    def edit_in_memory(r_id, field, new_val):
        c = CovidController.model.find_one_record("_id", int(r_id))
        r = Record()
        r.load_from_cursor(c)
        r.__dict__[str(field)] = str(new_val)
        return r

    @staticmethod
    def search_and_parameter(field1, param1,field2, param2):
        return CovidController.model.search_and(field1, param1,field2, param2)

    @staticmethod
    def search_or_parameter(field1, param1, field2, param2):
        return CovidController.model.search_or(field1, param1, field2, param2)

# CovidController.load_records()

# c = CovidController.select_all_records()
# for i in c:
#     print(i)

# cursor = CovidController.find_one_record("_id", "3")
# r = Record()
# r.load_from_cursor(cursor)
# r.__dict__[str("id")] = str("FDTE")
# r.pretty()
