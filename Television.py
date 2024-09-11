class Television :

    def __init__(self, make, model, size, color):
        self.make = make
        self.model = model
        self.size = size
        self.color = color

    def type(self):
        print(f"You own an {self.make} {self.model}")
        


Tv1 = Television("LG", "Flat_screen", 43, "Black")


Tv1.type()




