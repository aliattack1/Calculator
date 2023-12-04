# whats in this document?

**this document is going to show the algorithm of this calculator in its calculations to developers
so developers can easily understand codes in this repository so they can easily commit improvments to it
so if you are not a developer this document is not suitable for you (go read user_guide_document.md)**

# what is the main goal of the program?
**this program is going to be a calculator using console as interface getting inputs like this 
100+25+(10*24)-(10+(10+10)) and return its answer**

**the input shoud be able to have parantheses , one charecter operators , spaces , and wrongparts entered by a user
handling true ones erasing false ones and be able to calculate its answer**

# how is this working ( version 0.6 )

**at first it gets a string input from user in console 
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

- first we seperate the raw input into multiple parts keeping it in a list
- we start a loop that takes the most left number (first element in list) and the next number of it  giving it to callop method
- callop method gives these numbers to a function (operation) that it will pick from registered operations  by the operator character between those numbers the function  will calculate that part and will return answer as first number for next operation

### separating input string into a list of numbers and operators

**in this part we first check all operators in input getting their indexes and store this data in two list
then we start to seperate from left side using indexes of operators so the list of 10+20 would be**
    ['10', '+', '20']

### main loop
