   #  Assignment no. 5

  # Q1. Print the while loop in same line 

i = 1
while i < 2:
    print(f"Hello world {i}", end = " ")
    i += 1

#   Q2 print star pattern - using loops

  #  i.  print star pattern 

# n = 5

# for i in range(1 , n+1):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()

    #   ii. print inverted triangle

# n = 5

# for i in range(n , 0, -1):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()

    #  iii.  print pyramid pattern

# n = 5

# for i in range(1, n+1 ):
#     print(" " *( n-i ), end="")     # speces the star  this line
#     print("*" * (2 * i - 1))

#   Q3. Write a program to find the factorial of a given number.

# def factorial(n):
#     result = 1
#     while n > 0:
#         result *= n
#         n -= 1
#     return result

# print(factorial(5))

   #  Q4. count the number of vowels in a string

# my_string = "python by pranay hedaoo"
# vowels = "aeiou"
# count = 0

# for char in my_string:
#     if char.lower() in vowels:
#         count += 1
# print("number of vowels are ", count)

  # Q5. Find the longest word in a sentence using a for loop ?

# Sentence = "Python by pranay hedaoo"
# words = Sentence.split()
# longest_word = ""

# for word in words:
#     if len(word) > len(longest_word):
#         longest_word = word

# print("The longest word is: ", longest_word)

   #  Q6. "do while" loop in python - how to do it ?      

# while True:
#     num = int(input("Enter a number is greater than 10: "))

#     if num > 10:
#         print(f"Valid number entered: {num}")
#         break
#     else:
#         print("Number is not greater than 10, try again")

    # Q7. Write a program to print first N number in the Fibonacci sequence using a while loop

def fibonacci(n):
    a,b = 0,1
    count = 0
    while count < n:
        print(a)
        a,b = b , a+b
        count += 1

fibonacci(10)

# Define a list of items
items = ["apple", "banana", "cherry", "date"]

# For loop without parameters (directly looping over the list)
for item in items:
    print("Fruit:", item)
