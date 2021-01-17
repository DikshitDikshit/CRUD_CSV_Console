'''
Assignment 04
Author Dikshit Dikshit
'''

from time import sleep
from os import system, name


# this function clears the screen
def clear():
    if name == 'nt':
        _ = system('clear')


from assign4 import Assign4

class presentation:

    def __init__(self):
        self.assign = Assign4()

    """ this function displays menu options """

    def dispMenu(self):
        print("\nDeveloped by Dikshit Dikshit")
        print("1- to display records\n2- to enter a new record\n3- to edit an existing record")
        print(
            "4- to delete an existing record\n5- to save current records to a new file\n6- Reload the original "
            "Dataset\n"
            "7- Search on the basis of ID an Date\n8- Search on the basis of ID and Cases\n9- Search on the basis of "
            "ID and Deaths\n10- Exit\n\n")

    """ User input function """

    def userChoice(self):

        self.dispMenu()

        choice = input("Select option from the menu above: ")

        # runs the loop until the choice is 7 (exit)
        while choice != "10":

            # display records
            if choice == "1":
                self.assign.readAll()
                sleep(7)
            elif choice == "2":
                # prompt user for input for the new records
                ID = input("Enter ID: ")
                DATE = input("Enter DATE: ")
                CASES = input("Enter CASES: ")
                DEATHS = input("Enter DEATHS: ")
                NAME_FR = input("Enter NAME in French: ")
                NAME_EN = input("Enter NAME in English: ")
                # making a cases class's instance to pass it into insert method of assign3 class.
                case = Cases(ID, DATE, CASES, DEATHS, NAME_FR, NAME_EN)
                self.assign.insert(case)
                print("Your record is successfully added\n")
                sleep(5)

            elif choice == "3":

                # take input to update the record
                ID = input("Enter ID: ")
                DATE = input("Enter DATE: ")
                CASES = input("Enter CASES: ")
                DEATHS = input("Enter DEATHS: ")
                NAME_FR = input("Enter NAME in french: ")
                NAME_EN = input("Enter NAME in english: ")
                # making a cases class's instance to pass it into update method of assign3 class.
                case = Cases(ID, DATE, CASES, DEATHS, NAME_FR, NAME_EN)
                self.assign.update(case)
                print("Your record is successfully updated!")

                # prompt user for id and date(using both as key) and passing it to delete method of assign3 class
                # to delete the record
            elif choice == "4":

                ID = input("Enter ID: ")
                DATE = input("Enter DATE: ")

                self.assign.delete(ID,DATE)
                print("The record is successfully deleted!")
                sleep(5)
            # write the updated data into a new file
            elif choice == "5":
                self.assign.writeToFile()
                print("The records are successfully saved to a new file!")
                sleep(5)
            # reload the original data into the memory
            elif choice == "6":
                self.assign.backup()

                sleep(5)
            # Search on the basis of multiple columns at the same time, Option 1: on the basis of ID and Date.
            elif choice == "7":
                ID = input("Enter ID: ")
                Date = input("Enter DATE: ")
                self.assign.dateAndId(ID, Date)
            # Search on the basis of multiple columns at the same time, Option 2: on the basis of ID and Cases.
            elif choice == "8":
                ID = input("Enter ID: ")
                Cases = input("Enter Cases: ")
                self.assign.idAndCases(ID, Cases)
            # Search on the basis of multiple columns at the same time, Option 3: on the basis of ID and Deaths.
            elif choice == "9":
                ID = input("Enter ID: ")
                Deaths = input("Enter Deaths: ")
                self.assign.idAndDeaths(ID, Deaths)
            else:
                # exit
                return

            clear()
            self.dispMenu()
            choice = input("Enter your choice : ")
