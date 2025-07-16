class First:
    X = 50
    Y = 40
obj = First()
print(obj.Y)

    # Adding X and Y

class First:
    X = 50
    Y = 40

obj = First()
print(obj.X + obj.Y)

# class employees:
#     def putData(Self):
#         Self.id = int(input("Enter employee id: "))
#         Self.Name = input("Enter your name: ")
#         Self.Salary = int(input("Enter your salary: "))

#     def display(Self):
#         print("employee id: ", Self.id)
#         print("employee name: ", Self.Name)
#         print("employee salary: ",Self.Salary)

# a = employees()
# a.putData()
# a.display()

# class Student:
#     def __init__(Self , my_roll , my_name , my_marks):
#         Self.myrollno = my_roll
#         Self.myName = my_name
#         Self.myMarks = my_marks

#     def average(Self):
#         return sum(Self.myMarks) / len(Self.myMarks)
    
# first_Student = Student(1,"Pranay",[10,20,30,40,50])
# print(first_Student.myName)
# print(first_Student.average())
        
#     #Using list - creating student details

# student_1 = ["Madhav", 10]
# student_2 = ["Vishakha", 12]

# print(f"{student_1[0]} is in class {student_1[1]}")
# print(f"{student_2[0]} class is in {student_2[1]}")

     # Using oops - class details

# class Student:      # created class it is a blue print 
#      # init = initialise     #   self parameter = reference or connection btn class and function 
#     def __init__(self , full_name , class_grade , class_Percentage):    # Method
#           self.name = full_name     # attributes
#           self.grade = class_grade      
#           self.percentage = class_Percentage

#     def student_details(self):     # method
#          print(f"{self.name} is in class {self.grade}, with {self.percentage}% ")

# student1 = Student("Madhav" , 12 , 95)      # object - it is instance of class   creating a object
# #     print(student1.name , student1.grade , student1.percentage)        # calling name
# #  print(f"I am {student1.name} and my grade is {student1.grade} and my percentage is {student1.percentage}")
# student1.student_details()    # calling second function to 1st function  
# print(student1.__dict__)     #  print key and values form

# student1.percentage = 98     # modified values
# del student1.percentage      #  Delete attribute
# print(student1.__dict__)
# # print(student1.percentage)

# class Student:
#     def __init__(self,name,grade,percentage,team):
#         self.name = name
#         self.grade = grade
#         self.percentage = percentage
#         self.team = team

#     def student_details(self):
#         print(f"{self.name} is in class {self.grade}, with {self.percentage}% and is team {self.team}")

# Team = "A"   # Link variable from objects
# Team2 = "B"

# Student1 = Student("Madhav" , 11 , 96 , Team)
# student2 = Student("Kunal" , 10 , 85 , Team2)

# print(student2.team)
# Student1.student_details()
# student2.student_details()

    #  adding privious question in Abstraction  - Hiding details and show only functionality

# class Student:
#     def __init__(self,name,grade,percentage,team):
#         self.name = name
#         self.grade = grade
#         self.percentage = percentage
#         self.team = team

#     def student_details(self):
#         #  Hide in console from adding percentage + 2
#         print(f"{self.name} is in class {self.grade}, with {self.percentage + 2}% and is team {self.team}")     

# Team = "A"   # Link variable from objects
# Team2 = "B"

# Student1 = Student("Madhav" , 11 , 96 , Team)
# student2 = Student("Kunal" , 10 , 85 , Team2)

# print(student2.team)
# Student1.student_details()
# student2.student_details()


    #  adding privious question in Encapsulation - private body and access through the public method

# class Student:
#     def __init__(self,name,grade,percentage,team):
#         self.name = name
#         self.grade = grade
#         self.__percentage = percentage    #  double underscore limit access
#         self.team = team

#   #  access private body
#     def get_percantage(self):
#         return self.__percentage     # return function are required

#     def student_details(self):
#         print(f"{self.name} is in class {self.grade}, with {self.percentage}% and is team {self.team}")

# Team = "A"   # Link variable from objects
# Team2 = "B"

# Student1 = Student("Madhav" , 11 , 96 , Team)
# student2 = Student("Kunal" , 10 , 85 , Team2)

# # print(student2.team)
# # Student1.student_details()
# # student2.student_details()
# print(Student1.get_percantage())
# print(student2.get_percantage())

    #  adding privious question in Inheritance - acquired parent property and class to child class

          # Parent class   
# class Student:
#     def __init__(self,name,grade,percentage,team):
#         self.name = name
#         self.grade = grade
#         self.percentage = percentage
#         self.team = team

#     def student_details(self):
#         print(f"{self.name} is in class {self.grade}, with {self.percentage}% and is team {self.team}")

# Team = "A"   # Link variable from objects
# Team2 = "B"

# Student1 = Student("Madhav" , 11 , 96 , Team)
# student2 = Student("Kunal" , 10 , 85 , Team2)

# class graduate_student(Student):      #    graduate class acquired student class syntex
#     def __init__(self, name, grade, percentage, team , stream):
#         super().__init__(name, grade, percentage, team)    # call parent class
#         self.stream = stream   # new parameter in child class

#     def student_details(self):
#         super().student_details()
#         print(f"Stream is {self.stream}")

# grad_student = graduate_student("Pranay", 12 , 96 , Team , "PCM")  
# print(grad_student.stream)
# print(grad_student.__dict__)
# grad_student.student_details()


    #  adding privious question in Polymorphism - allow method in diff class have same name but duff behaviour

# class Student:
#     def __init__(self,name,grade,percentage):
#         self.name = name
#         self.grade = grade
#         self.percentage = percentage

#     def student_details(self):
#         print(f"{self.name} is in class {self.grade}, with {self.percentage}%")

# Student1 = Student("Madhav" , 11 , 96)
# student2 = Student("Kunal" , 10 , 85)

# class GraduateStudent(Student):
#     def __init__(self, name, grade, percentage, Stream):
#         super().__init__(name , grade , percentage)
#         self.stream = Stream

#     def student_details(self):    #  This is method
#          #super().student_details()
#          # print(f"{self.name} is in class {self.grade}, with {self.percentage}% and from stream {self.stream}")
#          print("Same method but sifferent output")

# #  object = student class

# Student1 = Student("Pranay" , 11 , 92 )

# #  object = graduate student class
# Grad_Student = GraduateStudent("Kunal" , 10 , 98 , "Pcm")

# Student1.student_details()
# Grad_Student.student_details()

# class ClassName:
#     def __init__(self, attribute1, attribute2):
#         self.attribute1 = attribute1
#         self.attribute2 = attribute2

#     def method(self):
#         print(f"Attribute1 is {self.attribute1} and Attribute2 is {self.attribute2}")

# my_dog = Dog("Buddy", "Golden Retriever")
# my_dog.bark()


# class Book:
#     def __init__(self, title, author, pages, genre):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.genre = genre

#     def book_details(self):
#         print(f"'{self.title}' by {self.author}, {self.pages} pages, Genre: {self.genre}")

# # Genre variables (like your Team and Team2)
# genre1 = "Science Fiction"
# genre2 = "Mystery"

# # Creating Book objects
# book1 = Book("Dune", "Frank Herbert", 412, genre1)
# book2 = Book("Sherlock Holmes", "Arthur Conan Doyle", 307, genre2)

# # Accessing one property
# print(book1.genre)

# # Calling method to display book details
# book1.book_details()
# book2.book_details()


from abc import ABC, abstractmethod

# -----------------------------
# Abstraction: Abstract Class
# -----------------------------
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method, must be overridden


# -----------------------------
# Base Class: Student (Encapsulation)
# -----------------------------
class Student:
    def __init__(self, name, grade, percentage):
        self.name = name
        self.grade = grade
        self.__percentage = percentage  # Encapsulated (private variable)

    def get_percentage(self):
        return self.__percentage  # Getter method

    def student_details(self):
        print(f"{self.name} is in class {self.grade}, with {self.get_percentage()}%")


# -----------------------------
# Derived Class: GraduateStudent (Inheritance + Polymorphism)
# -----------------------------
class GraduateStudent(Student):
    def __init__(self, name, grade, percentage, stream):
        super().__init__(name, grade, percentage)  # Call to base class constructor
        self.stream = stream  # Additional attribute

    # Polymorphism: overriding parent method
    def student_details(self):
        super().student_details()
        print(f"Stream: {self.stream}")


# -----------------------------
# Concrete Class: Rectangle (Implements abstract method)
# -----------------------------
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):  # Overriding abstract method
        return self.length * self.width


# -----------------------------
# Creating and Using Objects
# -----------------------------

# Encapsulation example
student1 = Student("Madhav", 11, 96)
student2 = Student("Kunal", 10, 85)

student1.student_details()
student2.student_details()
print("Accessing private data using getter:", student2.get_percentage())

# Inheritance & Polymorphism
grad_student = GraduateStudent("Pranay", 12, 92, "PCM")
grad_student.student_details()
print("Stream:", grad_student.stream)
print("Graduate student data:", grad_student.__dict__)

# Abstraction example
rect = Rectangle(10, 5)
print("Area of rectangle:", rect.area())
