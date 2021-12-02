import json

try:
    FName = "problem1.txt"
    File = open(FName, 'r')
    Data = File.read()
    print(json.loads(Data))
    DList = json.loads(Data)
    print(DList[1])
except:
    print("That file does not exist")
