"""
You are given a string where you have to find its first word.

- Input string consists of only english letters and spaces.
- There aren’t any spaces at the beginning and the end of the string.

first_word("Hello world") == "Hello"

How it is used: The first word is a command in a command line.
Precondition: Text can contain a-z, A-Z and spaces.
"""

def first_word(input: str):
  return input.split(' ', 1)[0]

value = input("Please enter a string:\n")

print(f'You entered {first_word(value)}')