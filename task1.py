"""
##### Task 1
Have the user enter in their name and email address.
Have the program create a file called 'task1.txt'
Write their name to the first line and their email to the second line.

Example:
What is your name? Joe Lunchbox
What is your email? joe@sandwiches.org 

task1.txt contents:
Joe Lunchbox
joe@sandwiches.org 
"""

filename = 'task1.txt'
file = open(filename,'w')

Name = input("What is your name? ")
file.write(Name + "\n")
Email = input("What is your email? ")
file.write(Email)