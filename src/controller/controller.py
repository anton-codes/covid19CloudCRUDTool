# Author: Anton Hrytsyk
import warnings

import pandas as pd
import pathlib

from model.datasetdf import DatasetDf
from model.record import Record

# DATASET represents the model
DATASET = DatasetDf(str(pathlib.Path(__file__).parent.parent.absolute()) + '/model/InternationalCovid19Cases.csv')

__doc__ = """
controller - accesses and manipulates data from the model
=====================================================================
Main Features
-------------
List of main features of controller:
  - Load records into active memory
  - Persist records from active memory into a new csv file
  - Persist records from active memory into the original csv file
  - CRUD in memory
  - CRUD directly to the csv file
--------------
@Author: Anton Hrytsyk   
"""


class Controller:
    # Path to a csv dataset
    CSV_DATASET = str(pathlib.Path(__file__).parent.parent.absolute()) + '/model/InternationalCovid19Cases.csv'

    @staticmethod
    def get_in_memory_records_list():
        """A list of records currently in active memory
        Returns:
            list: list of records currently in active memory
        """
        return DATASET.in_memory_records_list

    @staticmethod
    def add_new_record_into_memory(_id, id, date, cases, deaths, name_fr, name_en):
        """ Adds a new record to the dataset
            Parameters:
                _id (string): _id of the new record
                id (string): id of the new record
                date (string): date of the new record
                cases (string): cases of the new record
                deaths (string): deaths of the new record
                name_fr (string): name_fr of the new record
                name_en (string): name_en of the new record
        """
        DATASET.in_memory_records_list.append(Record(_id, id, date, cases,
                                                     deaths, name_fr, name_en))

    @staticmethod
    def select_and_edit_in_memory(_id, column, new_value):
        """ Updates record in the in_memory_records_list.

        Parameters:
            _id (string): _id of the record to be updated
            column (string): column_name of the column to be updated
            new_value (string): value that will be assigned to the record
                                with the specified _id @column_name

        """
        for record in DATASET.in_memory_records_list:
            if str(record._id) == str(_id):
                record.__dict__[str(column)] = str(new_value)
                return record
        return

    @staticmethod
    def load_into_memory():
        """ Loads 100 records from the dataset,
        loads each record into a DTO
        and stores them in a list structure

        Returns:
            list : list of 100 Record objects initialized from InternationalCovid19Cases.csv
        """
        dataframe = Controller.load_from_csv(100)
        DATASET.in_memory_records_list = Controller.load_into_records(dataframe)
        return DATASET.in_memory_records_list

    @staticmethod
    def search_in_memory(column, condition):
        """ Searches for a specific record or records in active memory
            Parameters:
                column (string): column_name of the column to search
                condition (string): condition, value @column_name to be selected
        """
        found_records = list()
        for record in DATASET.in_memory_records_list:
            if str(record.__dict__[column]) == str(condition):
                found_records.append(record)
        return found_records

    @staticmethod
    def delete_from_memory(_id):
        """ Deletes a specific record from active memory
        Parameters:
            _id (str): _id of the record to be deleted
        Returns:
              model.record: deleted record
        """
        for record in DATASET.in_memory_records_list:
            if str(record._id) == str(_id):
                DATASET.in_memory_records_list.remove(record)
                return record
        return -1

    @staticmethod
    def persist_records():
        """ Persists records from active memory into InternationalCovid19Cases.csv file """
        df = pd.DataFrame()
        for record in DATASET.in_memory_records_list:
            df.append(Controller.to_df(record._id, record.id, record.date,
                                       record.cases, record.deaths,
                                       record.name_fr, record.name_en))
        df.to_csv(Controller.CSV_DATASET, mode='a', header=False, index=False)

    @staticmethod
    def write_records_to_new_file(filename):
        """ Persists records from active memory into a new csv file
        Parameters:
            filename (str): filename of a new csv file
        """
        dataframe = pd.DataFrame(columns=['_id', 'id', 'date', 'cases',
                                          'deaths', 'name_fr', 'name_en'])
        for record in DATASET.in_memory_records_list:
            df = Controller.to_df(record._id, record.id,
                                  record.date, record.cases,
                                  record.deaths, record.name_fr,
                                  record.name_en)
            df.columns = ['_id', 'id', 'date', 'cases',
                          'deaths', 'name_fr', 'name_en']
            dataframe = dataframe.append(df, ignore_index=True)
        dataframe.to_csv(str(pathlib.Path(__file__).parent.parent.absolute()) + '/model/' + str(filename), mode='w',
                         columns=['_id', 'id', 'date', 'cases',
                                  'deaths', 'name_fr', 'name_en'],
                         sep=',', index=False, encoding='utf-8')

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
    def update_main_dataframe():
        """Updates the main programs dataframe with values from the dataset"""
        DATASET.dataframe = pd.read_csv(Controller.CSV_DATASET)
        return DATASET.dataframe

    @staticmethod
    def get_dataset():
        """Accessor for the DATASET object"""
        return DATASET

    # CRUD DIRECTLY INTO THE CSV

    @staticmethod
    def create_record(_id, id, date, cases, deaths, name_fr, name_en):
        """ Adds a new record to the dataset
        Parameters:
            _id (string): _id of the new record
            id (string): id of the new record
            date (string): date of the new record
            cases (string): cases of the new record
            deaths (string): deaths of the new record
            name_fr (string): name_fr of the new record
            name_en (string): name_en of the new record
        """
        df = Controller.to_df(_id, id, date, cases, deaths, name_fr, name_en)
        df.to_csv(Controller.CSV_DATASET, mode='a', header=False, index=False)

    @staticmethod
    def search_record(column_name, condition):
        """ Searches for a specific record or records in the dataset
        Parameters:
            column_name (string): column_name of the column to search
            condition (string): condition, value @column_name to be selected
        """
        Controller.update_main_dataframe()
        return Controller.get_dataset().dataframe.loc[Controller.get_dataset().dataframe[column_name] == condition]

    @staticmethod
    def delete_record(_id):
        """ Deletes record from the dataset
        Parameters:
            _id (string): _id of the record to be deleted
        """
        DATASET.commit_dataframe(DATASET.dataframe[DATASET.dataframe["_id"] != _id])

    @staticmethod
    def update_record(_id, column_name, value):
        """ Updates record in the dataset.

        Parameters:
            _id (string): _id of the record to be updated
            column_name (string): column_name of the column to be updated
            value (string): value that will be assigned to the record
                                with the specified _id @column_name

        """
        warnings.filterwarnings("ignore")
        df = Controller.search_record("_id", _id)
        df[column_name] = value
        Controller.delete_record(_id)
        df.to_csv(Controller.CSV_DATASET, mode='a', header=False, index=False)
        warnings.filterwarnings("default")

    @staticmethod
    def load_from_csv(n_lines):
        """ Reads data from the dataset

        Parameters:
            n_lines (int): number of rows from the dataset

        Returns:
            pandas.core.frame.DataFrame: A sample of the dataset

        """
        return DATASET.dataframe.head(n_lines)

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
