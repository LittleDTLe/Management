'''
TO DO:
-ADD AUTHENTICATION
-DO NOT SHOW PASSWORD
-CONNECTED WITH CSV / SQL BASE
-LOGGED IN STATUS
'''

import csv
from os import path
import os


class login():
    username = ""
    password = ""
    logged = False

    def __init__(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

    def log(self):
        self.fileExist()
        with open("credentials.csv", "r") as inp:
            for row in csv.reader(inp):
                if self.username in row[0] and self.password in row[1]:
                    self.logged = True
        return self.logged

    def fileExist(self):
        if not path.exists("credentials.csv"):
            f = open("credentials.csv", "w")
            f.write("USERNAME,PASSWORD")
            f.close()

    def createMan(self):
        self.copyCSV()
        inp = open("credentials_edit.csv", "r")
        out = open("credentials.csv", "a")
        username = input("Enter username: ")
        password = input("Enter password: ")
        data = {line[0] for line in csv.reader(inp)}
        if username not in data:
                out.write(username + "," + password  + "\n")
                print("WRITING")
        else:
            print("REGISTRATION NOT POSSIBLE USER ALREADY EXISTS!!!")
        inp.close()
        out.close()
        os.remove("credentials_edit.csv")
        

    def copyCSV(self):
        inp = open("credentials.csv", "r")
        out = open("credentials_edit.csv", "w", newline="")
        w = csv.writer(out)
        for row in csv.reader(inp):
            w.writerow(row)
        inp.close()
        out.close()