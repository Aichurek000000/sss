class Fruit:
    def __init__(self):
        self.mass = 0
class Apple(Fruit):
    color_option = ["red", "green"]
    def __init__(self, color):
        if color in self.color_option:
            self.color = color
        else:
            print("n")
class Orange(Fruit):
    color = ["orange"]
    def make_juice(self):
        self.juice = self.mass / 2
orange = Orange()
orange.mass = 150
orange.make_juice()
print(orange.juice)
