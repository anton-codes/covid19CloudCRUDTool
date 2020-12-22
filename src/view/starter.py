# Author Anton Hrytsyk
from controller.controller import Controller

__doc__ = """
The Starter contains methods to start the program.
This class performs read operation and is responsible for displaying the data.
=====================================================================
@Author: Anton Hrytsyk   
"""

from controller.covidController import CovidController
from model.FormattedRecord import FormattedRecord
from model.record import Record


class Starter:

    @staticmethod
    def print_cursor(cursor_obj):
        if isinstance(cursor_obj, dict):
            print(cursor_obj)
        else:
            for rec in cursor_obj:
                print(rec)

    @staticmethod
    def sortRecords(column_name):
        """
        Sorts records by column_name
        """
        dataframe = CovidController.get_loaded_records()
        print(dataframe.sort_values(by=[str(column_name)]).head(10))


    @staticmethod
    def print_records(record_data):
        """ Prints out record objects and all their fields """
        for record in record_data:
            print('--------------------------------------------------------------')
            for field, value in record.__dict__.items():
                print(str(field) + " : " + str(value))

    @staticmethod
    def submit_selection_new(selection):
        if selection == '1':
            CovidController.load_records()
            print("records from the csv were successfully loaded into the database")
        if selection == '2':
            Starter.print_cursor(CovidController.select_all_records())
        if selection == '3':
            # Anton Hrytsyk 040938383
            r_id = input("Enter record id: ")
            column = input("Enter column: ")
            new_val = input("Enter new value: ")
            CovidController.update_record(r_id, column, new_val)
            print("Record id: " + str(r_id) + " was successfully updated")
            Starter.print_cursor(CovidController.find_one_record("_id", r_id))
        if selection == '4':
            r_id = input("Enter id of the record you want to delete: ")
            CovidController.delete_record("_id", int(r_id))
            print("Record id: " + str(r_id) + " was successfully deleted")
        if selection == '5':
            column = input("Enter column: ")
            new_val = input("Enter value: ")
            Starter.print_cursor(CovidController.search_record(column, new_val))
        if selection == '6':
            print('Enter values for the new record')
            _id = input('_id: ')
            id = input('id: ')
            date = input('date: ')
            cases = input('cases: ')
            deaths = input('deaths: ')
            name_fr = input('name_fr: ')
            name_en = input('name_en: ')
            CovidController.insert_record(_id, id, date, cases, deaths, name_fr, name_en)
            print("Record was successfully inserted")
            Starter.print_cursor(CovidController.find_one_record('_id', int(_id)))
        if selection == '7':
            # Author: Anton Hrytsyk 040938383
            field1 = input("Enter column 1: ")
            val1 = input("Enter value for column 1: ")
            condition = input("and/or ")
            field2 = input("Enter column 2: ")
            value2 = input("Enter value 2: ")

            if condition.lower() == "and" :
                Starter.print_cursor(CovidController.search_and_parameter(field1, val1, field2, value2))
            else:
                Starter.print_cursor(CovidController.search_or_parameter(field1, val1, field2, value2))


        if selection == '0':
            column = input("enter column to sort by ")
            Starter.sortRecords(column)
            bool = input("Want to edit an in-memory record?")
            # Anton Hrytsyk 040938383
            if bool == "yes":
                r_id = input("enter record id of the record you wish to edit")
                field = input('enter column you wish to edit')
                new_val = input("enter new value for " + field)
                r = CovidController.edit_in_memory(r_id, field, new_val)
                print("Record successfully updated")
                print(r.pretty())
    # @staticmethod
    # def submit_selection(selection):
    #     """ Submits input from the user and relays it to the Controller with appropriate parameters """
    #
    #     if selection == '1':
    #         # Loads 100 records into active memory
    #         Controller.load_into_memory()
    #         print('in_memory records were successfully replaced with the records from the original dataset')
    #         print('==============================================================')
    #         print('Author: Anton Hrytsyk')
    #         print('==============================================================')
    #     elif selection == '2':
    #         filename = input('Enter the name of the file where you wish to save current records: ')
    #         Controller.write_records_to_new_file(filename)
    #         print('Records were successfully saved to src/model/' + str(filename))
    #         print('==============================================================')
    #         print('Author: Anton Hrytsyk')
    #         print('==============================================================')
    #     elif selection == '3':
    #         Controller.persist_records()
    #         print('Records were successfully saved to src/model/InternationalCovid19Cases.csv')
    #         print('==============================================================')
    #         print('Author: Anton Hrytsyk')
    #         print('==============================================================')
    #     elif selection == '4':
    #         print('Enter values for the new record')
    #         _id = input('_id: ')
    #         id = input('id: ')
    #         date = input('date: ')
    #         cases = input('cases: ')
    #         deaths = input('deaths: ')
    #         name_fr = input('name_fr: ')
    #         name_en = input('name_en: ')
    #         Controller.add_new_record_into_memory(_id, id, date, cases, deaths, name_fr, name_en)
    #         print('New record was successfully added to the in-memory list')
    #         print('==============================================================')
    #         print('Author: Anton Hrytsyk')
    #         print('==============================================================')
    #     elif selection == '5':
    #         _id = input('_id of the record you want to edit(in memory only): ')
    #         column = input("Select one of the columns: _id, id, date, cases, deaths, name_fr, name_en ")
    #         condition = input("Enter new value for _id: " + str(_id) + ' at ' + str(column) + ": ")
    #         Controller.select_and_edit_in_memory(_id, column, condition)
    #         print('Record updated successfully')
    #         print('==============================================================')
    #         print('Author: Anton Hrytsyk')
    #         print('==============================================================')
    #         return
    #     elif selection == '6':
    #         _id = input('_id of the record you want to delete(in memory only): ')
    #         Controller.delete_from_memory(_id)
    #         print("Record with _id:" + str(_id) + " was deleted successfully(in memory only)")
    #         print('==============================================================')
    #         print('Author: Anton Hrytsyk')
    #         print('==============================================================')
    #     elif selection == '0':
    #         Starter.print_records(Controller.get_in_memory_records_list())
    #         print('==============================================================')
    #         print('Author: Anton Hrytsyk')
    #         print('==============================================================')
    #     elif selection == '7':
    #         column = input("Select one of the columns: _id, id, date, cases, deaths, name_fr, name_en ")
    #         condition = input("Enter the value to search for: ")
    #         Starter.print_records(Controller.search_in_memory(column, condition))
    #         print('==============================================================')
    #         print('Author: Anton Hrytsyk')
    #         print('==============================================================')
    #     return

    @staticmethod
    def get_input():
        """ Gets input from the user """
        selection = '0'
        while str(selection) != '9':
            print('==============================================================')
            print('1. Upload/Re-upload records from the csv to the database')
            print('2. Display all from the database')
            print('3. Update a record')
            print('4. Delete a record')
            print('5. Search records')
            print('6. insert new record')
            print('7. search records on multiple parameters ')
            print('--------------------------------------------------------------')
            print('0. Load into memory and display all records(you can sort these)')
            print('9. Exit')
            print('==============================================================')
            print('Author: Anton Hrytsyk')
            print('==============================================================')
            selection = input('Enter selection: ')
            Starter.submit_selection_new(selection)


# main
if __name__ == "__main__":
    # Loads 100 records into active memory

    Starter.get_input()
    print('\n\n Anton Hrytsyk, student # 040938383')

    # r = FormattedRecord('1', 'AA', '2020.05.04', '1.0', '2.0', 'fr', 'en')
    # print(r.pretty())
