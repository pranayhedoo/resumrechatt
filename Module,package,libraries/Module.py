# Module :-  it is a single python file

import myModule       #full file import

myModule.say_hello("Madhav")

myModule.say_byee("Ishan")

from myModule import person1     # Specific line import 
print(person1["name"])

sample = "Hello World"

print("Original Text:", sample)
print("Uppercase:", myModule.to_upper(sample))
print("Lowercase:", myModule.to_lower(sample))
print("Number of vowels:", myModule.count_vowels(sample))
