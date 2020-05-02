"""
Try to find out how many zeros a given number has at the end.

end_zeros(0) == 1
end_zeros(1) == 0
end_zeros(10) == 1
end_zeros(101) == 0
"""


"""
Other solutions

def end_zeros(number):
    n = str(number)
    return len(n) - len(n.strip('0'))

def end_zeros(number):
    import re
    return len(re.search('0*$', str(number)).group())

def end_zeros(number):
    number = str(number)
    if number[-1:] != '0':
        return 0
    return 1 + end_zeros(number[:-1])

def end_zeros(number):
    if not number:
       return 1
    if not number % 10:
       return 1 + end_zeros(number // 10)
    return 0

def end_zeros(number):
    result = not number
    while number and not number % 10:
        number /= 10
        result += 1
    return result

def end_zeros(number):
    en = enumerate(str(number)[::-1])
    return not number or next(i for i, x in en if x != '0')

def end_zeros(number):
    from itertools import takewhile
    number = str(number)[::-1]
    return len(list(takewhile(lambda x: x == '0', number)))
"""

def end_zeros(num: int) -> int:
  total_zero = 0
  exit = False
  counter = len(str(num))

  while(counter>0 and exit == False):
    if(str(num)[counter - 1] == '0'):
      total_zero += 1
    else:
      exit = True

    counter -= 1

  return total_zero

# ------------------------------------------------ #

print(end_zeros(11010110))
print(end_zeros(1))
print(end_zeros(100000))