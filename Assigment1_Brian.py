class Student:
    def __init__(self, Course, Name, RegNo):
        self.Course = Course
        self.Name = Name
        self.RegNo = RegNo

    def display(self):
        print(f'Welcome {self.Name} RegNo: {self.RegNo} to {self.Course}')

RegNo = input('Please enter your RegNo: ')
Student_name = input('Pleade enter your Name: ')
Course = input('Pleade enter your Coure: ')

Student1 = Student(Course, Student_name, RegNo)

Student1.display()

