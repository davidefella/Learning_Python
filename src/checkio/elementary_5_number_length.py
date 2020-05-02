"""
You have a positive integer. Try to find out how many digits it has?

number_length(10) == 2
number_length(0) == 1
"""

def number_length(number: int) -> int:
  return len(str(number))

print(number_length(10) == 2)
print(number_length(0) == 1)