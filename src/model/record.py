# Author: Anton Hrytsyk
__doc__ = """
record - Data Transfer Object
=====================================================================
Represents a row in the dataset
--------------
@Author: Anton Hrytsyk   
"""


class Record:
    def __init__(self, _id='-1', id='-1', date='-1', cases='-1', deaths='-1', name_fr='-1', name_en='-1'):
        """ The Record object represents a single row in the dataset.
                :param id: The id is used for identifying a case
                :type id: str
                :param date: The date of a case
                :type date: str
                :param cases: number of cases
                :type cases: str
                :param deaths: number of deaths
                :type deaths: str
                :param name_fr: French name
                :type name_fr: str
                :param name_en: English name
                :type name_en: str
        """
        self._id = str(_id)
        self.id = str(id)
        self.date = str(date)
        self.cases = str(cases)
        self.deaths = str(deaths)
        self.name_fr = str(name_fr)
        self.name_en = str(name_en)

    def pretty(self):
        """ Pretty representation of an object.
                        :param id: The id is used for identifying a case
                        :type id: str
                        :param date: The date of a case
                        :type date: str
                        :param cases: number of cases
                        :type cases: str
                        :param deaths: number of deaths
                        :type deaths: str
                        :param name_fr: French name
                        :type name_fr: str
                        :param name_en: English name
                        :type name_en: str
                """
        print(self._id, self.id, self.date, self.cases, self.deaths, self.name_fr, self.name_en)

    def load_from_cursor(self, cursor_obj):
        """
        This method is to populate fields from a mongobd cursor object
        """
        self._id = str(cursor_obj['_id'])
        self.id = str(cursor_obj['id'])
        self.date = str(cursor_obj['date'])
        self.cases = str(cursor_obj['cases'])
        self.deaths = str(cursor_obj['deaths'])
        self.name_fr = str(cursor_obj['name_fr'])
        self.name_en = str(cursor_obj['name_en'])
