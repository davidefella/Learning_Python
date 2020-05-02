'''

Create a function that gets a tuple and returns a tuple with 3 elements - the first, third and second element from the last for the given array.

easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
easy_unpack((6, 3, 7)) == (6, 7, 3)
'''

#TIP: The main difference between lists and tuples is the fact that lists are mutable whereas tuples are immutable.
# ARRAY: a = ["apples", "bananas", "oranges"]
# TUPLE: a = ("apples", "bananas", "oranges")

# ALTERNATIVE SOLUTION
#from operator import itemgetter
#easy_unpack = itemgetter(0, 2, ~1)

def easy_unpack(elements):
  return elements[0], elements[2], elements[len(elements)-2]

print(easy_unpack((6, 3, 7)) == (6, 7, 3))
print(easy_unpack((1, 1, 1, 1)) == (1, 1, 1))
print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7))
