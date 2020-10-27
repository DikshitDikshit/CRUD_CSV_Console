'''
Assignment 02
Author Dikshit Dikshit
'''
from Application import ApplicationLayer
import unittest



class TestValidator(unittest.TestCase):

    # this function verifies if the data values read from the csv file matching with the data set
    def test_verifyDisplayedfirstRectoDataset(self):
        obj = ApplicationLayer("InternationalCovid19Cases.csv")
        rec = ['AD','2020-03-03',1,0,'Andorre','Andorra']
        list_r = [obj.ID[0], obj.DATE[0], obj.CASES[0], obj.DEATHS[0], obj.NAME_FR[0],
                  obj.NAME_EN[0]]

        self.assertEqual(rec[0], list_r[0])
        self.assertEqual(rec[1], list_r[1])
        self.assertEqual(rec[2], list_r[2])
        self.assertEqual(rec[3], list_r[3])
        self.assertEqual(rec[4], list_r[4])
        self.assertEqual(rec[5], list_r[5])
        print("Developed by Dikshit Dikshit")


if __name__ == '__main__':
    unittest.main()
