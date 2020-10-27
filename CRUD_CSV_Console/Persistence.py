"""
Assignment 02
Author Dikshit Dikshit
"""
import pandas as pd
""" using pandas because of it's high- performance in data analysis and it is easy to use with data structures also"""
class persistence:

    def __init__(self, filename):
        self.__mainFile = filename

    """ reads first 100 rows from file """
    def readData(self):
        return pd.read_csv(self.__mainFile, nrows=100)
    """ writes updated data to new file """
    def writeUpdatedRecord(self, rec, f_name):
        """ open the new file, if the file does not exist this will create a new file with read and write permissions"""
        file = open(f_name, "w+")
        """ write all the data to the new file as a comma separated file """
        file.write(
            "ID, DATE, CASES,DEATHS, NAME_FR, NAME_EN\n")
        for i in range(0, len(rec)):
            for j in range(0, len(rec[0])):
                file.write(str(rec[i][j]) + ",")
            file.write("\n")
        file.close()
