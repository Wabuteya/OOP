class Student :

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def info(self):
        print(f"I am {self.name} and i weigh at {self.weight}")

student1 = Student("John", 23, "50kgs")
student2 = Student("Joan", 20, "80kgs")

student1.info()
student2.info()