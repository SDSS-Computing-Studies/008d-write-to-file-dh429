#!python3
import json

'''
Ask the user to enter in a list of 5 words.
Convert the word to a string literal JSON object
Write the contents to a file called 'task3.txt'

Example:
Enter a word: frog
Enter a word: french
Enter a word: puppy
Enter a word: escalate
Enter a word: ice

task3.txt contents:
["frog","french","puppy","escalate","ice"]

'''
filename = 'task3.txt'
file = open(filename,'w')

wlist = []

for i in range(5):
    word = input("Enter a word: ")
    wlist.append(word)

WriteData = json.dumps(wlist)
file.write(f"{WriteData}")
