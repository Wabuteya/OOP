class Watch :

    def __init__(self, model, size, color):
        self.model = model
        self.size = size
        self.color = color

    def type(self):
        print(f"I own a {self.model} {self.color} smart watch")
        


watch1 = Watch("Samsung", 43, "Black")


watch1.type()

