  #  Q1 Limit the decimal places to 2 digits using format method and print results, for the variable pi=3.14159265359

pi = 3.14159265359

print("Value of pi us {:.2f}".format(pi))

  # Q2 Extract character from index 2 to 8 with a step of 2: Given my_strick = "python Course", slice character from index 2 to 8,
  #  skipping every other character 

my_string = "Pytho Course"
print(my_string[2:8:2])

    #  Q3. Slice to get only the middle character(s): for my_string = "madhav", use slicing to extract the middle character

my_String2 = "Madhava"
print(int(len(my_String2)/2))

   # Q4.  Remove the first 3 and last 3 character: Gien my_String = "Regression Analsis", remove the first 3 nad last 3 character

my_String3 = "Regression Analsis"
print(my_String3[3:-3])

   #  Q5. Get the substring that start 4 character from the end to the last character: For my_string = "Classification", 
   # slice the string starting from the 4th character and end with the last character

my_string4 = "Classification"
print(my_string4[-4:])

  #  Q6. How to reverse a string Using python String method

String = "Pranay"
print(String[::-1])

#  Q7. Write a python function to check if a string is a palindrom using String method.

my_String5 = "madam"
def is_palindrome(s):
    if s == s[::-1]:
     print("S is a palindrome")
    else:
      print("S is not a palindrome")

is_palindrome(my_String5)

