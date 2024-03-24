# gomu7109

import sqlite3 as sql
import json
from random import sample
from playsound import playsound
from colorama import Fore
from datetime import datetime

API = json.load(open("Src/Json/api.json"))
Num = "1234567890"

MENU = """
Make ID For TODO list   [1]
add Data in TODO list   [2]
Delete ID from database [3]
show todo list          [4]
Exit                    [0]
"""
connection = sql.connect(API["database"])
connect = connection.cursor()
Date = datetime.today().date()

class todo:
    def makeID(self, name):
        ID = ''.join(sample(Num, 4))
        playsound(API["soundOne"])
        return name+ID

    def addData(self, data, ID):
        connect.execute(f"INSERT INTO {ID} (Date, data) VALUES(?, ?)", (Date, data))

    def deleteTable(self, ID):
        connect.execute(f"DROP TABLE {ID}")
        playsound(API["soundTwo"])

    def fetchData(self, ID):
        connect.execute(f"SELECT * FROM {ID}")
        data = connect.fetchall()
        playsound(API["soundTwo"])
        return data


if __name__ == "__main__":
    while(True):
        print(Fore.GREEN, MENU, Fore.WHITE)

        server = todo() 

        numValue = input("Enter a Option : ")
        
        try:
            numValue = int(numValue)
        except(Exception):
            print(Fore.RED, "Enter valid value", Fore.WHITE)

        if numValue == 1:
            name = input("Enter name : ")
            id = server.makeID(name)
            connect.execute(f"CREATE TABLE {id} (Date text, Data text)")
            print(f"your ID is Create : {id}") 

        elif numValue == 2:
            ID = input("Enter your ID : ")
            try:
                i = int(input("aitems in list in number : "))
            except(Exception):
                print(Fore.RED, "Enter valid value", Fore.WHITE)

            List = []
            for i in range(i):
                List.append(input("Enter data : "))

            List = str(List)
            server.addData(List, ID)

        elif numValue == 3:
            ID = input("Enter your ID : ")
            conferm = input("Do You Want to Continew [y/n]: ")
            if conferm == 'y':
                server.deleteTable(ID)
                print(Fore.GREEN, "ID Deleted", Fore.WHITE)
            elif conferm == 'n':
                print(Fore.GREEN, "Thanks You For Confermetion", Fore.WHITE)

        elif numValue == 4:
            ID = input("Enter your ID : ")
            print(server.fetchData(ID))

        elif numValue == 0:
            connection.commit()
            connection.close()
            exit()

        else:
            print(Fore.RED, "Invalid Option", Fore.WHITE)

