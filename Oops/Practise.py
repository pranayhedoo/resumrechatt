#  Class  :- A class is a blueprint or template for creating objects 

# Object  :- An object is a specific instance of a class

# Student details

# Student_1 =[ "Madhav" , 10 ]
# Student_2 = ["Vishakha" , 12]

# print(f"{Student_1[0]} Student is in a {Student_1[1]}")
# print(f"{Student_2[0]} Student is in a {Student_2[1]}")

#   USing oops
# class Student:  # class creation
#     def __init__(self , name , grade , Percenatge):    # value initialise
#         self.name = name                  #  attribute
#         self.grade = grade 
#         self.percentage = Percenatge                 #  attribute                # Class ->  Method -> Attribute  -> Object creation

#     def student_details(self):    #   This is method
#         print(f"{self.name} is in class {self.grade}, with {self.percentage}%")

# Student_2 = Student("Vishakha" , 20 , 75)

# Student_1 = Student("Madhav" , 15 , 91)  # object creation

# Student_1.student_details()
# Student_2.student_details()

# print(Student_1.__dict__)    # output is in Dictonary

# #print(Student_1.name , Student_1.grade)



# class Student:
#     def __init__(self , name , grade , percentage , team):
#         self.name = name 
#         self.grade = grade
#         self.__percentage = percentage
#         self.team = team

#     def get_percentage(self):
#         return self.__percentage           #For acces throufg the private method

#     def student_details(self):
#         print(f"{self.name} is in class {self.grade}, with {self.percentage+2}% and is in team {self.team}")     +2  hidden hote percentage mdhe

# team1 = "A" 
# team2 = "B"

# Student1 = Student("Madhav" , 10 , 68 , team1)
# Student2 = Student("Vishakha" , 12 , 79 , team2)

# Student1.student_details()
# Student2.student_details()

# print(Student1.team)


  #  4 feature in oops

  #  1. Abstraction   :-  Hiding unnecessary details from users through class , method 

  #  2. Encapsulation  :- Restrick the asscess to certain attributes or method to protect data for enforce controlled access

  #  3. Inheritance  :- allows one class to reuse property and method of another class   
    
 #    Ex. Class Parent(Child):   self replace to super().__init__() for accessing

  #  4. Ploymorphism :-allows method in diff. class to have same name bit diff. baheviour depending on objects