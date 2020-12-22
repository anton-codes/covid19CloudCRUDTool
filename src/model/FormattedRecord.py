from model.record import Record


# Anton Hrytsyk 040938383

class FormattedRecord(Record):

    def __init__(self, _id, id, date, cases, deaths, name_fr, name_en):
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
        super().__init__(_id, id, date, cases, deaths, name_fr, name_en)

    def pretty(self):
        """
        Pretty representation of an object
        """
        s = ""
        for field, value in self.__dict__.items():
            s += ( str(field) + " : " + str(value) + " \n" )
        return s




