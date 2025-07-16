class Student:
    def __init__(self,name,grade,percentage):
        self.name = name
        self.grade = grade
        self.percentage = percentage

    def student_details(self):
        print(f"{self.name} is in class {self.grade}, with {self.percentage}% ")

class graduate_student(Student):      #    graduate class acquired student class syntex
    def __init__(self, name, grade, percentage , stream):
        super().__init__(name, grade, percentage)    # call parent class
        self.stream = stream   # new parameter in child class

    def student_details(self):
        super().student_details()
        print(f"Stream is {self.stream}")

grad_student = graduate_student("Pranay", 12 , 96 , "PCM")  
print(grad_student.stream)
print(grad_student.__dict__)
grad_student.student_details()