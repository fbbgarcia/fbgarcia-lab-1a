# CSC 365 Lab 1 Part a: Why Databases?
This program searches a students.txt file by user command and outputs the results of the search.


## Featured Commands:
[] indicate optional input
- S[tudent]: LASTNAME
  - returns the name, grade, classroom, and teacher of each student found with the given last name
- S[tudent]: LASTNAME B[us]
  - prints the name and bus of each student found with the given last name
- T[eacher]: LASTNAME
  - returns the name of each student found with teachers of the given last name
- G[rade]: BUS#
  - returns the name of each student found in the given grade level 
- B[us]: BUS#
  - returns the name, grade, and classroom of each student found who takes the given bus route
- G[rade]: GRADE# [H[igh]|L[ow]]
  - returns the name, GPA, teacher, and bus route of the student in the given grade with the highest or lowest grade GPA found
- A[verage]: GRADE#
  - returns the average GPA of the given grade level (rounded to two decimal places)
- I[nfo]
  - returns the number of students in each grade level ranging from 0 to 6
- Q[uit]
  - quit the current session of the program


## Instructions:
Run the schoolsearch.py script. Make sure to have a students.txt file in the same directory. Enter one of the above commands after the prompt. That's it!
