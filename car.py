class car :

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def own(self):
        print(f"You own a {self.make} {self.model}")

    def drive(self):
        print(f"You drive a {self.make} {self.model}")

    def describe(self):
        print(f"This is a {self.year} {self.make} {self.model}")

car1 = car("Toyota", "Mark_X", 2019, "Black")


car1.own()
car1.drive()
car1.describe()


