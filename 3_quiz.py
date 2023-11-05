class Rectangule:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        print(self.width * self.height)
    

obj = Rectangule(2,2)
obj.calculate_area()