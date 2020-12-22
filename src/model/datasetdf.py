import pandas as pd

__doc__ = """
dataset_df - abstraction of the model
=====================================================================
Main Features
-------------
List of main features of dataset_df:
  - Singleton (only one for the entire program)
  - Holds in-memory data (used for in-memory CRUD by the controller)
  - Holds main dataframe (used for direct CRUD by the controller)
--------------
@Author: Anton Hrytsyk   
"""


def singleton(dataset_df):
    """ Singleton method
    Returns:
        getInstance().
    """
    instances = {}

    def getInstance(*args, **kwargs):
        """ getInstance method
            Returns:
                current instance.
            """
        if dataset_df not in instances:
            instances[dataset_df] = dataset_df(*args, **kwargs)
        return instances[dataset_df]

    return getInstance


@singleton
class DatasetDf(object):
    # main dataframe
    dataframe = ''
    # path to the csv file
    csv_path = ''
    # records in active-memory
    in_memory_records_list = list()
                                                        # ANTON HRYTSYK (hryt0001) 040938383
    def __init__(self, csv_path):
        """
        Handles file IO on initialization
        """
        self.csv_path = csv_path
        try:
            self.dataframe = pd.read_csv(csv_path)
        except FileNotFoundError:
            print('ERROR: File not found')

    def commit_dataframe(self, dataframe):
        """ Update the main dataframe
        Parameters:
            dataframe new main dataframe
        """
        self.dataframe = dataframe
        dataframe.to_csv(self.csv_path, index=False, sep=',')
