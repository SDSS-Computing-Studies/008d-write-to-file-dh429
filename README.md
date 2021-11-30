## SDSS Computing Studies Python Assignment
### Assignment #8d Write to a File (Total Marks 10)

Objectives:
* Read data from a file
* Store data to a file
* Develop an understanding of javascript object notation (json)
* Use the json library to retrieve or store complex data structures

We sometimes refer to volatile memory as memory stores where information is impermanent - when you turn off your computer, or when you close the program, the data stored in memory is gone.  There are several ways to deal with volatile memory that you want to keep:
1. We can save it to a file
2. We can store it in a database (which is really saving it to a file in a database)

Old methods would store the value of one variable per line in a text file, but these are very limited in their use.  It also doesn't really work well for more complex data structures like lists or tuples.  

##### Javascript Object Notation (JSON) #####
https://en.wikipedia.org/wiki/JSON
JSON is a way of storing complex data into text.  It is so useful that it has become quite standard to pass complex data between different applications using JSON.  A web page which uses Javascript to run its applications might send a request to a server that runs on Python or PHP.  That site will send data as JSON to the web page, where it is decoded and utilized in the Javascript environment.  JSON is very useful as a cross platform way of communicating! 

Today we will be reading and writing data from files.  There are many ways to read data from a file:
* You can read a whole file into a single variable
* You can read a file one line at a time, and store each line as an element of a list

### 2 Tasks

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

(3 points) 

##### Task 2
Tell the user that they will be entering in a list of integers.
Keep reading integers until they enter a blank line (press Enter)
Write the value of each integer to a new line of a text file called 'task2.txt'

Example:
Enter integers. Press Return to exit.
Enter a number: 2
Enter a number: 3
Enter a number: 4
Enter a number: 25
Enter a number: 1
Enter a number: 2
Enter a number: 3
Enter a number: 4
Enter a number: 5

task2.txt contents:
2
3
4
25
1
2
3
4
5

(3 points)

##### Task 3
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

(3 points) 

##### Problem 1
When the program loads, check to see if the file problem1.txt exists. If it does, see if the data can be interpreted using json.  


##### Problem 2
Write a program to keep track of your current grades for 8 subjects.  Create a menu system that lets a user do the following:
1. Change the name of their subjects
2. Enter in a new value for their grade
3. Read data from a file
4. Save the current data to a file.

