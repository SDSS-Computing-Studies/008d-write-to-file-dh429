#!python3
import json

x = 10
y = 3
z = ['Hello','world']
ad = ['test']
outputData = json.dumps(z)
outputData = json.dumps(ad)

print(type(z))
print(type(outputData))
print(outputData)

file = open('example2.txt','w')
file.write(f"{outputData}")
file.close()

readfile = open('example2.txt','r')
newList = readfile.read()
jsonList = json.loads(newList)
print(type(newList))
print(type(jsonList))
print(jsonList)
print(jsonList[0])
