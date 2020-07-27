# Chapter 3 - Functions

This serves as the documentation for the practice projects under this folder. Feel free to correct me for errors that I may have committed. Contact me through email at masterjed7262@gmail.com

## Collatz Sequence

Taken from the book, this program aims to do the following.

> Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and return 3 \* number + 1.

_Additional instructions_:

> Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1.

We signify the intent of the program with the `print` statement at line 3 but the actual input is at `line 13`. We define the function `collatz` which essentially does two things.

1. If a number is divisible by 2, return the result after dividing.
2. If a number is not divisible by 2, return that is `3` times the `number + 1`.

`Line 17` initiates a loop which keeps calling the function until the `result` equals to 1.

## Input Validation

Taken from the book, this program aims to do the following,

> Add try and except statements to the previous project to detect whether the user types in a noninteger string. Normally, the int() function will raise a ValueError error if it is passed a noninteger string, as in int('puppy'). In the except clause, print a message to the user saying they must enter an integer.

We define the function `validate()` at `Line 6`. This function is in a forever loop that won't stop until you input an `int`. At `Line 13`, we handle what happens when a user does not input an integer. We print out an error message and we ask for input again until the user successfully enters an `int`.

---

Last Edited: 07/27/20 3:37 PM
