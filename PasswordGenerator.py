import string
from random import sample

caps = string.ascii_uppercase
small = string.ascii_lowercase
numbers = string.digits
symbols = string.punctuation
combination = caps + small + numbers + symbols
password = input("Which type of password you want ? \nWeak or Strong ? ").lower()
if password == "strong":
    print("".join(sample(combination, 8)))
else:
    print("".join(sample(combination, 2)))
