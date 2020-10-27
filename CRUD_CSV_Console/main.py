'''
Assignment 02
Author Dikshit Dikshit
'''
from Presentation import presentation

""" 
begins the application by calling presentation's init method 
"""
def main():

    obj = presentation("InternationalCovid19Cases.csv")
    obj.userChoice()


main()
