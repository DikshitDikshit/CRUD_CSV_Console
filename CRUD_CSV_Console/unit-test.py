'''
Assignment 03
Author Dikshit Dikshit
'''
import unittest
from assign4 import Assign3
from cases import Cases
import sqlite3

class TestValidator(unittest.TestCase):
    # this function verifies if the data values added to the database are same that we passed to it.
    def testInsertRecord(self):
        obj = Assign3()
        rec = ['aa','2020-01-01',1,0,'French','English']
        case = Cases(rec[0], rec[1], rec[2], rec[3], rec[4], rec[5])
        obj.insert(case)
        conn = sqlite3.connect('covid_cases.db')
        db = conn.cursor()
        db.execute("SELECT * FROM CovidCases WHERE id=? AND date=?", ('aa', '2020-01-01'))
        record = db.fetchone()
        conn.commit()
        self.assertEqual(rec[0], record[0])
        self.assertEqual(rec[1], record[1])
        self.assertEqual(rec[2], record[2])
        self.assertEqual(rec[3], record[3])
        self.assertEqual(rec[4], record[4])
        self.assertEqual(rec[5], record[5])
        print("Developed by Dikshit Dikshit")


if __name__ == '__main__':
    unittest.main()
