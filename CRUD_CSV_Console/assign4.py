'''
Assignment 04
Author Dikshit Dikshit
'''
import sqlite3
import csv as csv

'''
using sqlite3 library to achieve the database CRUD goal.
'''
'''
connecting to the database, if database doesn't exist it'll create one for you
after establishing the connection with the database, creating table in it with the same column name as we have in the 
csv file, by using execute() method which executes the query in the database.
'''
conn = sqlite3.connect('covid_cases.db')
db = conn.cursor()
db.execute('''
  CREATE TABLE IF NOT EXISTS CovidCases (
      id char(2) NOT NULL,
      date DATE NOT NULL,
      cases INTEGER NOT NULL,
      deaths INTEGER NOT NULL,
      name_fr varchar(255) NOT NULL,
      name_en varchar(255) NOT NULL
      )
''')
'''
loading the data from csv file to the database table, to prevent the data adding repetition we are first clearing the 
data from the table then adding by executing executemany() method which takes 2 arguments, one is the query, and another
one is rows from the database table, actual values of each row will replace the "?"s in the query.
at the end committing the changes to the database
'''
a_file = open("InternationalCovid19Cases.csv")
rows = csv.reader(a_file)
with conn:
    db.execute("DELETE FROM CovidCases")
db.executemany("INSERT INTO CovidCases VALUES (?, ?, ?, ?, ?, ?)", rows)

conn.commit()

class Assign4():

    conn = sqlite3.connect('covid_cases.db')
    db = conn.cursor()
    '''
    this method Searches on the basis ID and Date of and display all the results from the database using 
    "SELECT * from TableName where clause and AND keyword to use multiple columns at the same time query 
    and printing the records one by one. 
    '''
    def dateAndId(self, id, date):
        j = 0
        db.execute("""SELECT * from CovidCases WHERE id = :id AND date = :date """, {'id': id, 'date': date})
        records = db.fetchall()
        print("ID,DATE,CASES,DEATHS,NAME_FR,NAME_EN")
        for row in records:
            if j % 10 == 0:
                print("Developed by Dikshit Dikshit")
            j += 1
            print(row[0] + "," + str(row[1]) + "," + str(row[2]) + "," + str(row[3]) + "," + row[4] + "," + row[5])

    '''
    this method Searches on the basis ID and Cases of and display all the results from the database using 
    "SELECT * from TableName where clause and AND keyword to use multiple columns at the same time query 
    and printing the records one by one. 
    '''
    def idAndCases(self, id, cases):
        j = 0
        db.execute("""SELECT * from CovidCases WHERE id = :id AND cases = :cases """, {'id': id, 'cases': cases})
        records = db.fetchall()
        print("ID,DATE,CASES,DEATHS,NAME_FR,NAME_EN")
        for row in records:
            if j % 10 == 0:
                print("Developed by Dikshit Dikshit")
            j += 1
            print(row[0] + "," + str(row[1]) + "," + str(row[2]) + "," + str(row[3]) + "," + row[4] + "," + row[5])

    '''
    this method Searches on the basis ID and Deaths of and display all the results from the database using 
    "SELECT * from TableName where clause and AND keyword to use multiple columns at the same time query 
    and printing the records one by one. 
    '''
    def idAndDeaths(self, id, deaths):
        j = 0
        db.execute("""SELECT * from CovidCases WHERE id = :id AND deaths= :deaths """, {'id': id, 'deaths': deaths})
        records = db.fetchall()
        print("ID,DATE,CASES,DEATHS,NAME_FR,NAME_EN")
        for row in records:
            if j % 10 == 0:
                print("Developed by Dikshit Dikshit")
            j += 1
            print(row[0] + "," + str(row[1]) + "," + str(row[2]) + "," + str(row[3]) + "," + row[4] + "," + row[5])

    '''
    adding new record using insert sql statement and commit changes after adding to the database.
    actual values of each record is stored i a tuple which is the second argument that we are passing, will replace the 
    "?"s in the query respectively.
    '''
    def insert(self, cases):
        db.execute("INSERT INTO CovidCases VALUES (?,?,?,?,?,?)", (cases.id, cases.date, cases.cases, cases.deaths,
                                                                       cases.name_fr, cases.name_en))

        conn.commit()
    '''
    updating a record using update sql statement and commit changes after adding to the database.
    actual values of each record is stored in a dictionary which will replace the ":____"s in the query by matching the
    keys in the dictionary.
    '''
    def update(self, cases):
        with conn:
                db.execute("""UPDATE CovidCases SET cases = :cases, deaths = :deaths, name_fr = :name_fr, 
                name_en = :name_en WHERE id = :id AND date = :date """, {'id': cases.id, 'date': cases.date
                                            ,'cases': cases.cases, 'deaths': cases.deaths, 'name_fr': cases.name_fr
                                            ,'name_en': cases.name_en})
    '''
    deleting a record using delete sql statement and commit changes after adding to the database.
    passing a dictionary which has the value ID and date of the record which we want to delete and those values 
    are passed to the query for "Where" clause to locate the record
    '''
    def delete(self, id, date):
            with conn:
                db.execute("DELETE FROM CovidCases WHERE id = :id AND date = :date", {'id': id, 'date': date})

    '''
    this method display all the records from the database using "SELECT * from TableName" query and printing the records
    one by one.
    '''
    def readAll(self):
            j = 0
            sqlite_select_query = """SELECT * from CovidCases"""
            db.execute(sqlite_select_query)
            records = db.fetchall()
            print("ID,DATE,CASES,DEATHS,NAME_FR,NAME_EN")
            for row in records:
                if j % 10 == 0:
                    print("Developed by Dikshit Dikshit")
                j += 1
                print(row[0] + "," + str(row[1]) + "," + str(row[2]) + "," + str(row[3]) + "," + row[4] + "," + row[5])
                print("\n")
    '''
    reload the previous data from the csv file by deleting the current data and inserting the old data. with exception 
    handling of file not found exception
    '''
    def backup(self):
        try:
            file = open("InternationalCovid19Cases.csv")
            row = csv.reader(file)
            with conn:
                db.execute("DELETE FROM CovidCases")
            db.executemany("INSERT INTO CovidCases VALUES (?, ?, ?, ?, ?, ?)", row)
            conn.commit()
            print("The records are successfully backedup!")
        except:
            print("Something went wrong")
    '''
    this method writes the current data to a new csv file by reading the data first from the table and then loading into
    a new file, this code will create a file if it doesn't exist and "," separated formatting is done automatically by writerows()
    method in csv library.
    '''
    def writeToFile(self):
        data = db.execute("SELECT * FROM CovidCases")
        with open('UpdatedRecords.csv', 'w+') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'date', 'cases', 'deaths', 'name_fr', 'name_en'])
            writer.writerows(data)
