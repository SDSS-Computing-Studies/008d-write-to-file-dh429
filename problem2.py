#!python3
import json
"""
##### Problem 2
Write a program to keep track of your current grades for 8 subjects.  Create a menu system that lets a user do the following:
1. Change the name of their subjects
2. Enter in a new value for their grade
3. Read data from a file
4. Save the current data to a file.

["Intro Spanish", "87", "Drafting", "100", "New Media", "83", "Computer Science", "100", "Psychology", "85", "Pre-Calculus", "79", "Law Studies", "84", "Biology", "90"]

"""

FName = "problem2.txt"
File = open(FName, 'r')
Data = File.read()
DList = json.loads(Data)

def menu():
    global DList
    global File
    while True:
        print("Here are your courses and your grades")
        print(f"{DList[0]}: {DList[1]}")
        print(f"{DList[2]}: {DList[3]}")
        print(f"{DList[4]}: {DList[5]}")
        print(f"{DList[6]}: {DList[7]}")
        print(f"{DList[8]}: {DList[9]}")
        print(f"{DList[10]}: {DList[11]}")
        print(f"{DList[12]}: {DList[13]}")
        print(f"{DList[14]}: {DList[15]}")

        print("[1] Change the name of a subject")
        print("[2] Change the value of a grade")
        print("[3] Reset any changes made")
        print("[4] Save the current data to a file")
        Choice = input("Enter in a selection: ")

        if Choice == "1":
            Running = True
            while Running:
                Found = 0
                SubChange = input("What subject would you like to change?: ")
                for i in range(len(DList)):
                    if SubChange in DList[i]:
                        Found = Found + 1
                        ListSlot = i
                if Found == 0:
                    print("That subject does not exist")
                if Found == 1:
                    Change = input("What would you like to change it to?: ")
                    DList[ListSlot] = Change
                    Running = False
                if Found > 1:
                    print("They're are multiple results with that search, please be more specific")
        if Choice == "2":
            Running = True
            while Running:
                Found = 0
                GradeChange = input("What subject grade would you like to change?:")
                for i in range(len(DList)):
                    if GradeChange in DList[i]:
                        Found = Found + 1
                        ListSlot = i + 1
                if Found == 0:
                    print("That subject does not exist")
                if Found == 1:
                    Change = input("What will be the new grade?: ")
                    DList[ListSlot] = Change
                    Running = False
                if Found > 1:
                    print("They're are multiple results with that search, please be more specific")
        if Choice == "3":
            FName = "problem2.txt"
            File = open(FName, 'r')
            Data = File.read()
            DList = json.loads(Data)
           
        if Choice == "4":
            FName = "problem2.txt"
            File = open(FName, 'w')
            OutputData = json.dumps(DList)
            File.write(f"{OutputData}")
            File.close()
            break
            
menu()