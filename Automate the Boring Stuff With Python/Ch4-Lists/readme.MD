# Chapter 4 - Lists

This serves as the documentation for the practice projects under this folder. Feel free to correct me for errors that I may have committed. Contact me through email at masterjed7262@gmail.com.

## Comma Code

Taken from the book, this program aims to do the following:

> Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.

In `Lines 4-8`, we define some lists that we can pass in the function that we are gonna create. The `enumerate` function takes in a list, and depending on the number of items in the list, prints out the items separated with `commas` and/or `and`.

_Note:_ We can instead ask the user for what list to view, however, that requires the lists to be mapped with the input string using a `dict`, something that hasn't been covered in this chapter. As such, we are hard coding what list to pass in to the function. This still accomplishes the intended instruction.

## Coin Flip Streaks

Taken from the book, this program aims to do the following:

> Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of heads and tails. Your program breaks up the experiment into two parts: the first part generates a list of randomly selected 'heads' and 'tails' values, and the second part checks if there is a streak in it. Put all of this code in a loop that repeats the experiment `10,000` times so we can find out what percentage of the coin flips contains a streak of six heads or tails in a row.

To start off, at `Line 3`, we import the `random` module to handle the generation of `heads` and `tails` in the forms of `0` and `1`.

Our main program essentially does two things:

1. Generate a list of 100 items, either being `H` or `T`.
2. Check if a streak of `6` heads or tails occur.

`Lines 10-14`: We have a loop that runs 100 times and each time it runs, it generates a `random number` using `random.randint`. Depending on the number that was produced, we append `H` or `T` to `master_list`.

`Lines 16:20`: Per item, we check up to the next 5 items whether they're all `H` or `T`. _We used `94` because if we used a value higher than that, we'll encounter the `IndexError`_. Once a streak is found, the counter variable (`number_of_streaks`) is incremented by `1`.

Finally, we take this `number_of_streaks` and divide by `10,000` then multiply `100` to get the percentage. Take note that we used 'f-strings` instead of the traditional formatting the author used in the book.

For more information on `f-strings`, check this: <https://realpython.com/python-f-strings/>

The result is most probably around `80%`.

## Character Picture Grid

Taken from the book, this program aims to transform the given list into a heart-looking list.

`Lines 18:21`: We loop over each item in each list. We print each list's `1st item` **( [0][0], [1][0], ..., [9][0] )** then enter a new line, then print each list's `2nd item` **( [0][1], [1][1], ..., [9][1] )** and enter another line. You get the idea. This continues until each item of each list has already been printed.

---

Last Edited: 07/27/20 5:22 PM
