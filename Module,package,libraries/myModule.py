def say_hello(name):
    return print(f"Hello {name}, what heppen!")

def say_byee(name):
    return print(f"Bye {name}, take care")

person1 = {"name" : "Pranay Hedaoo" , "Age" : 25}

def to_upper(text):
    return text.upper()

def to_lower(text):
    return text.lower()

def count_vowels(text):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)
