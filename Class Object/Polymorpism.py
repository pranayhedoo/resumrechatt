class Student:
    def __init__(self,name,grade,percentage):
        self.name = name
        self.grade = grade
        self.percentage = percentage

    def student_details(self):
        print(f"{self.name} is in class {self.grade}, with {self.percentage}%")

class GraduateStudent(Student):
    def __init__(self, name, grade, percentage, Stream):
        super().__init__(name , grade , percentage)
        self.stream = Stream

    def student_details(self):    #  This is method
         print("Same method but different output")

#  object = student class

Student1 = Student("Pranay" , 11 , 92 )

#  object = graduate student class
Grad_Student = GraduateStudent("Kunal" , 10 , 98 , "Pcm")

Student1.student_details()
Grad_Student.student_details()