# whats in this document?

**this document is going to show the algorithm of this calculator in its calculations to developers
so developers can easily understand codes in this repository so they can easily commit improvments to it
so if you are not a developer this document is not suitable for you (go read user_guide_document.md)**

# what is the main goal of the program?
**this program is going to be a calculator using console as interface getting inputs like this 
100+25+(10*24)-(10+(10+10)) and return its answer**

**the input shoud be able to have parantheses , one charecter operators , spaces , and wrongparts entered by a user
handling true ones erasing false ones and be able to calculate its answer**

# how is this working ( version 0.8 )

**at first it gets a string input from user in console then the program checks if input have paranthese if it has a loop will 
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
- then callop method gives these numbers to a function (operation) that it will pick from registered operations  by the operator character between those numbers the function  will calculate that part and will return answer as first number for next operation

### separating input string into a list of numbers and operators

**in this part we first check all operators in input getting their indexes and store this data in two list
then we start to seperate from left side using indexes of operators so the list of 10+20 would be**
    ['10', '+', '20']

### main loop
**in main loop we send first number and second one  with their operator in between to callop function**

**this function will choose one of operators (an operator function) from operator string and gives it numbers (functions are stored in a dict with the string of their operator)**

**operator functions will calculate the answer and return it (if we have a negetive number from inside a parantheses it will calculate that too**

**then the main loop uses the answer returned as left number and calculates it with next number and operator using same callop function**

## registraion of operators

**in calculator class we need to fill the dict countainig operators so we have a loop that for all submited methods in operations package in __init__.py adds the function with key of its operator string to that dict**

# what this program cant still do

**this program is still having problem with user wrong inputs and etc...**
