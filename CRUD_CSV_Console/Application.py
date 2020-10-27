'''
Assignment 02
Author Dikshit Dikshit
'''
from Persistence import persistence
class ApplicationLayer:
    """
    in this functions in persistence class are used to read data from csv file

    """
    def __init__(self, filename):
        self.pers = persistence(filename)
        self.record = self.pers.readData()
        self.record.fillna(" ")

        self.storeData()

    """
    This function stores the read data frame into a List using iloc
    
    """

    def storeData(self):
        self.ID = list(self.record.iloc[:, 0])
        self.DATE = list(self.record.iloc[:, 1])
        self.CASES = list(self.record.iloc[:, 2])
        self.DEATHS = list(self.record.iloc[:, 3])
        self.NAME_FR = list(self.record.iloc[:, 4])
        self.NAME_EN = list(self.record.iloc[:, 5])

        self.len = len(self.ID)

    """ this function displays all the records  i.e 100 """

    def display(self):
        j = 0
        print(
            "ID  DATE  CASES  DEATHS  NAME_FR  NAME_EN     \n\n")
        for i in range(0, self.len):

            if j % 10 == 0:
                print("Developed by Dikshit Dikshit")
            j += 1
            string = str(self.ID[i]) + " " + str(self.DATE[i]) + " " + str(self.CASES[i]) + " " + str(
                self.DEATHS[i]) + " " + str(self.NAME_FR[i]) + " " + str(self.NAME_EN[i])
            print(string + "\n")

    """ update a record on the basis of ID and Date as a key"""

    def update(self, l_rec):
        ind = 0
        inb = 0
        try:
            for i in self.ID:
                if i == l_rec[0]:
                    for j in self.DATE:
                        if j == l_rec[1]:
                            if ind < self.len-1:
                                ind = ind + inb
                            self.CASES[ind] = l_rec[2]
                            self.DEATHS[ind] = l_rec[3]
                            self.NAME_FR[ind] = l_rec[4]
                            self.NAME_EN[ind] = l_rec[5]
                            return 1
                        inb = inb + 1
                ind = ind + 1
            return -1
        except:
            return -1
    """ this function adds the record and checks if it already exists """
    def addRec(self, l_rec):
        ind = None
        try:
            for i in self.ID:
                if i == l_rec[0]:
                    for j in self.DATE:
                        if j == l_rec[1]:
                            return -1
            for i in self.ID:
                if i != l_rec[0]:
                    self.ID.append(l_rec[0])
                    self.DATE.append(l_rec[1])
                    self.CASES.append(l_rec[2])
                    self.DEATHS.append(l_rec[3])
                    self.NAME_FR.append(l_rec[4])
                    self.NAME_EN.append(l_rec[5])
                    self.len = 1 + self.len
                    return 1
            for i in self.ID:
                if i == l_rec[0]:
                    for j in self.DATE:
                        if j != l_rec[1]:
                            self.ID.append(l_rec[0])
                            self.DATE.append(l_rec[1])
                            self.CASES.append(l_rec[2])
                            self.DEATHS.append(l_rec[3])
                            self.NAME_FR.append(l_rec[4])
                            self.NAME_EN.append(l_rec[5])
                            self.len = 1 + self.len
                            return 1
        except:
            self.ID.append(l_rec[0])
            self.DATE.append(l_rec[1])
            self.CASES.append(l_rec[2])
            self.DEATHS.append(l_rec[3])
            self.NAME_FR.append(l_rec[4])
            self.NAME_EN.append(l_rec[5])
            self.len = 1 + self.len
            return 1

    """ delete a record using ID and Date as a key """

    def deleteRec(self, l_rec):
        ind = 0
        inb = 0
        try:
            for i in self.ID:
                if i == l_rec[0]:
                    for j in self.DATE:
                        if j == l_rec[1]:
                            if ind < self.len-1:
                                ind = ind + inb
                            self.ID.pop(ind)
                            self.DATE.pop(ind)
                            self.CASES.pop(ind)
                            self.DEATHS.pop(ind)
                            self.NAME_FR.pop(ind)
                            self.NAME_EN.pop(ind)
                            self.len = self.len -1
                            return 1
                        inb = inb + 1
                ind = ind + 1
            return -1

        except:
            return -1

    """
    this function writes the data from memory to a new file 
    
    """

    def writeFile(self):
        l_rec = []

        for i in range(0, self.len):
            dict = []
            dict.append(self.ID[i])
            dict.append(self.DATE[i])
            dict.append(self.CASES[i])
            dict.append(self.DEATHS[i])
            dict.append(self.NAME_FR[i])
            dict.append(self.NAME_EN[i])

            l_rec.append(dict)
        self.pers.writeUpdatedRecord(l_rec, "updated.csv")
