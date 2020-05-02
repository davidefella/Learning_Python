"""
In this mission you need to create a password verification function.

Those are the verification conditions:

- the length should be bigger than 6.
"""
def is_acceptable_password(password: str) -> bool:
  return (len(password)>6)


print(is_acceptable_password('short') == False)
print(is_acceptable_password('muchlonger') == True)
