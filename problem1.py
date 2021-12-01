import json

try:
    FName = "problem1.txt"
    File = open(FName, 'r')
    Data = File.read()
    print(json.loads(Data))
except:
    print("That file does not exist")
