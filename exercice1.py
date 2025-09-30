# True is a specific boolean value
print(True == True)    # Output: True
print(1 == True)       # Output: True (because 1 is exactly equal to True)
print(2 == True)       # Output: False (because 2 is not exactly True)

# Truthy values
if 2:
    print("2 is truthy")  # This will print because 2 is truthy

if "":
    print("This won't print")  # An empty string is considered False (falsy)
else:
    print("Empty string is falsy")  # This will print

# You can also check if a value is truthy or falsy by using bool():
print(bool(2))  # Output: True (because 2 is truthy)
print(bool(0))  # Output: False (because 0 is falsy)
print(bool("Hello"))  # Output: True (non-empty string is truthy)
print(bool(""))  # Output: False (empty string is falsy)