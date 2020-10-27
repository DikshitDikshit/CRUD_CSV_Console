'''
Assignment 02
Author Dikshit Dikshit
'''

from time import sleep
from os import system, name


# this function clears the screen
def clear():
    if name == 'nt':
        _ = system('clear')


from Application import ApplicationLayer


class presentation:

    def __init__(self, fname):
        self.app = ApplicationLayer(fname)

    """ this function displays menu options """

    def dispMenu(self):
        print("Developed by Dikshit Dikshit")
        print("1- to display records\n2- to enter a new record\n3- to edit an existing record")
        print(
            "4- to delete an existing record\n5- to save current records to a new file\n6- Reload the orignal Dataset\n7-exit\n\n")

    """ User input function """

    def userChoice(self):

        self.dispMenu()

        choice = input("Select option from the menu below: ")

        # runs the loop until the choice is 7 (exit)
        while choice != "7":

            # display records
            if choice == "1":
                self.app.display()
                sleep(7)
            elif choice == "2":
                # prompt user for input for the new records
                ID = input("Enter ID: ")
                DATE = input("Enter DATE: ")
                CASES = input("Enter CASES: ")
                DEATHS = input("Enter DEATHS: ")
                NAME_FR = input("Enter NAME in french: ")
                NAME_EN = input("Enter NAME in english: ")

                if self.app.addRec(
                        [ID, DATE, CASES, DEATHS, NAME_FR, NAME_EN]) == -1:
                    print("The record you entered already exists, Try with new values")
                else:
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

                if self.app.update(
                        [ID, DATE, CASES, DEATHS, NAME_FR, NAME_EN]) == -1:
                    print("The Data you entered doesn't exists in our records!")
                else:
                    print("Your record is successfully updated!")
                sleep(5)
                # prompt user for id and date(using both as key) to delete the record
            elif choice == "4":

                ID = input("Enter ID: ")
                DATE = input("Enter DATE: ")

                if self.app.deleteRec([ID, DATE]) == -1:
                    print("Information you entered doesn't exist in our records!")
                else:
                    print("The record is successfully deleted!")
                sleep(5)

            elif choice == "5":
                # write the updated data into a new file
                self.app.writeFile()
                print("Data loaded to new file!")
                sleep(2)
            elif choice == "6":
                # reload the original data into the memory
                self.app.storeData()
                print("Data is reloaded from the previous file")
                sleep(2)
            else:
                # exit
                print("\nProcess finished with exit code 0")

                return

            clear()
            self.dispMenu()
            choice = input("Enter your choice : ")
