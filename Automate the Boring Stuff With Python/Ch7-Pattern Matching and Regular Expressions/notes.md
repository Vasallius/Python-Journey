# Chapter 7

To be able to use regex functions we must first `import re` 

* `re.compile()` accepts a string value and returns a Regex pattern object
* `/d` is a digit character
* `search` method searches the string passed into it 
  * returns None if *regex* pattern not found
  * if **found**, returns a *match* object 
    * *match* object has `group()` method that returns the actual matched text
    * `group()` can take in integers to specify what group to take
      * passing in **0**, returns entire matched text
    * `groups()` returns all groups
* `mo` is a generic name to use for ***match objects***
* adding **( )** will create **groups**
  * ex: (\d\d\d)-(\d\d\d-\d\d\d\d)
* multiple-assignment trick 
  * `a,b = mo.groups()`
* escape character = `\`
* `|` = **pipe**, used to match either expressions
  * `findall()` finds all matching occurrences
* `?` = optional matching preceding `?` 
* `*` = match zero or more preceding `*` 
* `+` = match one or more preceding `+` 
* `{}` are used to match with repetition 
  * ex: `{3}` or `{3, 5}` or `{, 5}` or `{3, }` 
* Regular expressions are **greedy** by default
  * `?` used for **lazy** matching

- | \d   | Any numeric digit from 0 to 9.                               |
  | ---- | ------------------------------------------------------------ |
  | \D   | Any character that is *not* a numeric digit from 0 to 9.     |
  | \w   | Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.) |
  | \W   | Any character that is *not* a letter, numeric digit, or the underscore character. |
  | \s   | Any space, tab, or newline character. (Think of this as matching “space” characters.) |
  | \S   | Any character that is *not* a space, tab, or newline.        |

- We can define our own character classes
  - ex: [a-zA-z0-9]

- `^` when placed at the opening of a the bracket, matches anything that is ***not*** in the character class
- `^` = beginning of text (placed at the beginning)
- `$` = end of text (placed at the end)
- `.` = wildcard character, match any character except newline

- can pass `re.DOTALL` as second argument to `re.compile` to match ***all*** characters
- regex is ***case-sensitive*** , pass `re.IGNORECASE` as second argument to `re.compile` to be ***case-insensitive*** 