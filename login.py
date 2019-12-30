'''
TO DO:
-ADD AUTHENTICATION
-DO NOT SHOW PASSWORD
-CONNECTED WITH CSV / SQL BASE
-LOGGED IN STATUS
'''

import csv
from os import path


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
                if self.username == row[0] and self.password == row[1]:
                    logged = True
                    return logged

    def fileExist(self):
        if not path.exists("credentials.csv"):
            f = open("credentials.csv", "w")
            f.write("USERNAME,PASSWORD")
            f.close()

    def createMan(self):
        with open("credentials.csv", "r") as inp:
            user = login.login()
            for row in csv.reader(inp):
                if user.username != row[0]:
                    with open("credentials.csv", "a") as out:
                        out.write(user.username + "," + user.password)
                else:
                    print("REGISTRATION NOT POSSIBLE USER ALREADY EXISTS!!!")