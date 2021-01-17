'''
Assignment 03
Author Dikshit Dikshit
Pure object class to access Each field of a record
'''

class Cases():

    def __init__(self,id,date,cases,deaths,name_fr,name_en):
        self.id = id
        self.date = date
        self.cases = cases
        self.deaths = deaths
        self.name_fr = name_fr
        self.name_en = name_en