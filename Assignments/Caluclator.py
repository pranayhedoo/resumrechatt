  # Q1  Calculator

    # Step-1

def Addition(num1 , num2):
 return num1 + num2

def Subtract(num1 , num2 ):
  return num1 - num2

def Multiplication(num1 , num2):
  return num1 * num2

def Divide(num1 , num2):
  return num1 / num2

def Average(num1 , num2):
  return (num1 + num2)/2

   # step-2

print("Please select a operation:\n "\
      "1. Addition\n"\
      "2.Substration\n"\
      "3. Multiplication\n"\
      "4.Divide\n"\
      "5.Average\n")

Select = int(input("Select a operation from 1,2,3,4,5: "))

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

  # step-3

if Select == 1:
  print(number1, "+", number2, "=", Addition(number1, number2))

elif Select == 2:
  print(number1, "-", number2, "=", Subtract(number1,number2))

elif Select == 3:
  print(number1, "*",number2, "=",Multiplication(number1,number2))

elif Select == 4:
  print(number1, "/", number2, "=", Divide(number1,number2))

elif Select == 5:
  print("(",number1, "+",number2,")", "/", "2", "=",Average(number1,number2))

else :
  print("Invalid operation please select again")