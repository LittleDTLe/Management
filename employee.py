'''
TO DO: 
-ADD A MENU
-IF NOT LOGGED IN YOU CAN ONLY SEARCH FOR AN EMPLOYEE AND 
THE RESULTS WILL BE LIMITED ex: NAME JOB TITLE ID YEARS IN COMPANY
'''

import login
import csv
import os.path
from os import path
from os import remove

class Employee():
    #Variables
    id = 0
    name = ""
    age = 0
    job = ""
    salary = 0
    years = 0
    rating = 0

    #Initialization of Object using Constructor
    def __init__(self):
        self.id = input("Enter ID: ")
        self.name = input("Enter name: ")
        self.age = input("Enter age: ")
        self.job = input("Enter job title: ")
        self.salary = input("Enter salary: ")
        self.years = input("Enter years in company: ")
        self.rating = input("Enter rating: ")
    
    #Checks if -employees.csv- file exists. If not it get created.
    def fileExist(self):
        if not path.exists("employees.csv"):
            f = open("employees.csv", "w")
            try:
                f.write("ID,Name,Job Title,Age,Salary,Years in Company,Rating" + "\n")
                print("Successful Submition!")
            except:
                print("Unsuccessful Submition!")
            f.close()


    #Function that is used to store information of employee in CSV file.
    def store(self):
        self.fileExist()
        f = open("employees.csv", "a")
        f.write(self.id + "," + self.name + "," + self.job + "," + self.age + "," + self.salary + "," + self.years + "," + self.rating)
        f.close()
    
    #Function that reads the CSV file where the employee info is stored.
    #Will be used to extract info from specifi employees and format it.
    def stored(self):
        f = open("employees.csv")
        csv_f = csv.reader(f)
        for row in csv_f:
            print('{:<10} {:<30} {:<30} {:<15} {:<20} {:<20} {:<15}'.format(*row))

    #Is supposed to delete a row from the CSV file where ID == delId.
    #I want it to be in the same file.
    #The way it is, it will transport all rows where ID != delId to another file.
    #One way to do it so that in the end it will be in the same file would be to then again
    #transport the data to the starter file.
    def deleteEntry(self):
        self.stored()
        delId = input("Enter employee ID: ")
        inp = open("employees.csv", "r")
        out = open("employees_edit.csv", "w", newline='')
        writer = csv.writer(out)
        for row in csv.reader(inp):
            if row[0] != delId:
                writer.writerow(row)
        inp.close()
        out.close()
        self.transporter()

    #Moves the data that is now in -employees_edit.csv-, NEW DATA WITHOUT DELETED ROW, back to -employees.csv-
    def transporter(self):
        inp = open("employees_edit.csv", "r")
        out = open("employees.csv", "w", newline='')
        writer = csv.writer(out)
        for row in csv.reader(inp):
            writer.writerow(row)
        inp.close()
        out.close()
        os.remove("employees_edit.csv")


#ONLY FOR TESTING PURPOSES IS IT HERE.
#THE MAIN PROGRAM WILL BE RUN IN ANOTHER FILE
login = login.login()
logged = login.log()
me = Employee()
if logged:
    login.login.createMan()
    me.store()
    me.deleteEntry()
    me.stored()