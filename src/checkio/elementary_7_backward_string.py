"""
You should return a given string in reverse order.

backward_string('val') == 'lav'
backward_string('') == ''
backward_string('ohho') == 'ohho'
backward_string('123456789') == '987654321'
"""

def backward_string(input: str) -> str:
    return input[::-1]

# ---------------------------------



print(  "1234567890"[::-1]        )


"""
print(backward_string('val') == 'lav')
print(backward_string('') == '')
print(backward_string('ohho') == 'ohho')
print(backward_string('123456789') == '987654321')
"""