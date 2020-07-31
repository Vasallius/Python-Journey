# Chapter 6 - Manipulating Strings

This serves as the documentation for the practice projects under this folder. Feel free to correct me for errors that I may have committed. Contact me through email at masterjed7262@gmail.com.

## **Table Printer**

In its very essence, this program takes a list of lists and prints it nicely.

`Line 3:` We set the needed data for this program

`Lines 7-14:` We create `length` a list that will contain the lengths of each word, which will be used to figure out what `int` we pass into to `.rjust()`. Using the `max()` function we are able to know the length of the longest word.

`Lines 17-21:` We loop over the number of items (creating 4 rows) and then the number of lists (3 items per row) to create a beautiful table like this.

```python
apples   Alice    dogs
oranges    Bob    cats
cherries Carol   moose
banana   David   goose
```

## **Zombie Dice Bots**

**Before trying to run the program, please make sure that you have the `zombiedice module`\* installed.**

\*_If you you don't have it yet, you can go the `terminal` or `command prompt` and type `pip install zombiedice`_.

In this program, we learn to create our own bots using different classes, however object oriented programming (OOP) is not explained in this book. As such a template has been provided for us to work on.

Things that you have to remember:

- `zombiedice.roll()` rolls the dice and returns the result in the variable `dice_roll_results`.
- `dice_roll_results` is a dictionary containing the number of `brains`, `fottsteps`, and `shotguns`.

We will be using these values as well as some random integers to aid the bot's decision whether to roll or not.

### **random_roller**

Bot Description: A bot that, after the first roll, randomly decides if it will continue or stop.

To do this functionality, after the first roll, we initiate a variable (`decision`) that contain either `0` or `1` using `random.randint(0,1)`.

`Line 30:`We initialize a `while` loop to keep rolling whenever `decision` equals to `0`.

### **stop_after_two_brains**

Bot Description: A bot that stops rolling after it has rolled two brains.

To do this, we first keep track of the number of brains via `brain_count`. As long as `dice_roll_results` does not return `None`, we add the number of `brains` collected from the roll to `brain_count`. However, the bot would only roll if `brain_count` is less than `2` as specified in `Line 50`.

### **stop_after_two_shotguns**

Bot Description: A bot that stops rolling after it has rolled two shotguns.

Similar to the bot above, we keep track of the number of shotguns via `shotgun_count`. We increment this value based on the number of shotguns retrieved from `dice_roll_results`. The bot will only roll if `shotgun_count` is less than `2` as specified in `Line 68`.

### **roll_one_to_four**

Bot Description: A bot that initially decides it’ll roll the dice one to four times, but will stop early if it rolls two shotguns.

This bot's roll based on a random predefined number of rolls `or` when it reaches `2` shotguns. We determine the number of rolls this bot will make using `random.randint(1,4)`. We will loop through that given number and roll each time. The bot stops to roll when `shotgun_count` equals to `2` as specified in `Line 95`.

### **shotgun_over_brain**

Bot Description: A bot that stops rolling after it has rolled more shotguns than brains.

We keep track of the number of brains and shotguns via `brain_count` and `shotgun_count`. We add whatever results we get from `dice_roll_results` and we only roll if the number of `shotguns` is less than the number of `brains`, as specified in `Line 117`. As you can see this strategy is very absurd, and if you run the simulator this bot will **NEVER** win.

Lastly, we add all the bots we made to the `zombies` tuple at `Line 126` and specify its name that will appear on the simulator.

---

Last Edited: 07/31/2020 11:10 PM
