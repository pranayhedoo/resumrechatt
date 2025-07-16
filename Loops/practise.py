# There are 5 types 
    #   Loops and Types
    #   While loops
    #   For Loops
    #   Range function
    #   Lopps Control Statement

#  1. While Loops
#    Its run jeva prient false nhi hot teva prient

# count = 2
# while count < 5:
#     print(count)
#     count = count + 1

# count = 1
# while count < 6:
#       print(count)
#       count += 1

# count = 5
# while count > 0:
#       print(count)
#       count -= 1

     # For Loops

language = "Python"  #sequence
for x in language:
     print(x)

# for i in range(5,10):  # range is start and stop
#     print(i)

# for i in range(5,10,2):  # range is start and stop and last is gap for 2
#      print(i)

# for i in range(5):
#     print(i)
# else:
#     print("for loops ended")

    #  Loops Control Statement

    # they are support 3 causes 
    
#     pass statement :-   It is use for future use

# for i in range(5):     Simple statement
#   pass

# count = 5 
# while count > 0:
#   if count == 3:
#     pass
#   else:
#     print(count)
#   count -= 1

#     break statement  :-  the break statement terminates the loop entirely, exiting from it immidiately

# for i in range(6):
#   if i == 5:
#     break
#   print(i)

#     continue statement  :- skip the current iteration and move to the next.

# for i in range(5):
#   if i == 3:
#     continue
#   print(i)

      #    Example 

# while True:
#     User_input = input("Enter 'exit' or stop: ")
#     if User_input == 'exit':
#      print("congrtas! you guessed is right")
#      break
#     print("Sorry, you entered: ", User_input)

# words = [
#     "level", "hello", "world", "radar", "python", "civic", "loop", "madam", "refer", "code"
# ]

# print("Palindromic words in the list:")
# for word in words:
#     if word == word[::-1]:
#         print(f"➡️  {word}")

# Program to generate Fibonacci sequence up to n terms using a while loop

# n_terms = int(input("Enter the number of Fibonacci terms to display: "))

# # First two terms
# a, b = 0, 1
# count = 0

# if n_terms <= 0:
#     print("Please enter a positive integer.")
# else:
#     print("Fibonacci sequence:")
#     while count < n_terms:
#         print(a, end=" ")
#         a, b = b, a + b
#         count += 1

# Simple while loop to print numbers from 1 to 10

# count = 1

# while count <= 10:
#     print(count)
#     count += 1  # This increases the value of count by 1 each time

def print_even_numbers(limit):
    """Prints even numbers up to a specified limit."""
    for number in range(limit + 1):
        if number % 2 != 0:
            print(number)

# Example usage: prints even numbers from 0 to 10
print_even_numbers(10)