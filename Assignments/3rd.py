  #  Q1

# year = int(input("Enter Year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): 
#     print(f"{year} is leaf year")
# else:
#     print(f"{year} is not a leaf year")

  #  Q2 

# predifinedUsername = 'Pranay'
# predifinedPassward = 'Pass2000'

# username = input("Enter your username: ")
# passward = input("Enter your Passward: ")

# if username == predifinedUsername:
#     if passward == predifinedPassward:
#         print("Welcome Your logined succesfully")
#     else:
#         print("passward are incorrect")
# else:
#     print("Invalid username")

  #  Q3 

mathMarks = int(input("Enter your Math: "))
physicsMarks = int(input("Emter your physics marks: "))
chemistryMarks = int(input("Enter you chemistry marks: "))

if (mathMarks >= 65 & physicsMarks >= 55 & chemistryMarks >= 50 \
    & (mathMarks + physicsMarks + chemistryMarks) >= 180 ) \
      or (mathMarks + physicsMarks) >= 140: 
    print("YOu are eligible")
else:
    print("You are not eligible")