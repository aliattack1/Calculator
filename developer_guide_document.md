# whats in this document?

**this document is going to show the algorithm of this calculator in its calculations to developers
so developers can easily understand codes in this repository so they can easily commit improvments to it
so if you are not a developer this document is not suitable for you (go read user_guide_document.md)**

# what is the main goal of the program?
**this program is going to be a calculator using console as interface getting inputs like this 
100+2!!5+(10*24)-(2log17+(10+10))+5sin30 and return its answer**

**the input shoud be able to have parantheses , one charecter operators , multi charecter known functions , spaces , and wrongparts entered by a user
 and be able to calculate its answer or raise a describing error**

# how is this working ( version 1.5 )

**at first it gets a string input from user in a tkinter based interface 
it will check input for unfinished parentheses and letters if any one of them seen it raises an error describing the problem
then it will deletes all spaces in input
then the program checks if input have paranthese if it has a loop will 
start**

- has parantheses
  - seperate in first parantheses
  - has parantheses
    - ......
  - answer seperated part
  - return answer to higher level
- answer seperated part
- return answer to console

**so this can handle the parantheses ( when we seperate inside of a paranthese we keep the right and left of it for when answer of parantheses came back)
but how is answer provided ?**

## calculating answer algorithm

- at first we order the operations
- then we seperate the raw input into multiple parts keeping it in a list
- then we start a loop that takes the most left number (first element in list) and the next number of it  giving it to callop method
- then callop method gives these numbers to a function or operation that it will pick from registered operations and functions  by the operator character or function string between those numbers the operator or function  will calculate that part and will return answer as first number for next one

### separating input string into a list of numbers and operators

**in this part we first check all operators in input getting their indexes and store this data in two list
then we start to seperate from left side using indexes of operators so the list of 10+20 would be**
    ['10', '+', '20']

### main loop
**in main loop we send first number and second one  with their operator in between to callop method or callfu method**

**this method will choose one of operators or functions from operator string and function list and gives it numbers (functions and operators are stored in a dict with the string of their operator)**

**operators or functions will calculate the answer and return it (if we have a negetive number from inside a parantheses it will calculate that too**

**then the main loop uses the answer returned as left number and calculates it with next number and operator using same callop method or callfu method**

## registraion of operators and functions

**in calculator class we need to fill the dict countainig operators so we have a loop that for all submited methods in operations package in __init__.py adds the function with key of its operator string to that dict**

## there are some copied from real calculator buttons in interface

## notice that some methods like input checker are imported from utility package
