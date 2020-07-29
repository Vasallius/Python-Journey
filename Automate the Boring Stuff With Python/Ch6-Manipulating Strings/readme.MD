# Chapter 5 - Manipulating Strings

This serves as the documentation for the practice projects under this folder. Feel free to correct me for errors that I may have committed. Contact me through email at masterjed7262@gmail.com.

## Table Printer

In its very essence, this program takes a list of lists and prints it nicely.

`Line 3:` We set the needed data for this program

`Lines 7-14:` We create `length` a list that will contain the lengths of each word, which will be used to figure out what `int` we pass into to `.rjust()`. Using the `max()` function we are able to know the length of the longest word.

`Lines 17-21:` We loop over the number of items (creating 4 rows) and then the number of lists (3 items per row) to create a beautiful table like this.

``` python
apples   Alice    dogs
oranges    Bob    cats
cherries Carol   moose
banana   David   goose
```

---
Last Edited: 07/28/2020 2:07 PM  
