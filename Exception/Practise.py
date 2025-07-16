# A = int(input("Enter value: "))
# B = int(input("Enter values: "))
# try:
#   C = A/B
#   print(C)
# except:
#   print("Exception Raised")
# finally:
#   print("End Porgram")

# try:
#     # Code that might raise an exception
#     num = int(input("Enter a number: "))
#     result = 10 / num
#     print(f"Result is {result}")
# except ValueError:
#     # This block will run if input is not an integer
#     print("Invalid input! Please enter a valid number.")
# except ZeroDivisionError:
#     # This block will run if user tries to divide by zero
#     print("Cannot divide by zero!")
# finally:
#     # This block will always run
#     print("Execution completed.")

# try:
#     num = int(input("Enter number: "))
#     result = 10 / num
#     print(f"Result is {result}")
# except ValueError:
#     print("Enter a integer values")
# except ZeroDivisionError:
#     print("Your enter zero Please enter Integer")
# finally:
#     print("Program termineted")

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: You can't divide by zero!")
except ValueError:
    print("Error: Please enter valid integers.")
except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    print("Execution finished.")
