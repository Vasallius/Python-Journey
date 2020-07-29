# Chapter 5 - Dictionaries and Structuring Data

This serves as the documentation for the practice projects under this folder. Feel free to correct me for errors that I may have committed. Contact me through email at masterjed7262@gmail.com.

## Fantasy Game Inventory

Taken from the book, this program aims to do the following:

>Write a function named displayInventory() that would take any possible “inventory” and display it like the following:

``` python
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62
```

`Line 5:` We simply input the given dictionary we have.

`Lines 7-13:` We define a function that takes in a given iterable (in this case a `dict`). We loop over each item in the dictionary using `for k,v`. These two variables represent each key and value per item in the dictionary. At `Line 12`, we increment the total number of items based on the `value`.

We call this function and its output should look something like this:

``` python
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62
```

## List to Dictionary Function

Taken from the book, this program aims to do the following:
> Write a function that takes in a `dict` object containing items to be added to the current inventory.

The `display_inventory` function is taken from the previous exercise, **Fantasy Game Inventory**.

`Lines 13-16`: We take each item in the given dictionary and make it a `key` in the current inventory. If it still doesn't exist yet, we assign the value `0` using the `.get()` method then add `1` to it. If it exists, then add `1`. This way we can handle existing items and non-existing items.

---

Last Edited: 07/28/2020 1:30 PM
