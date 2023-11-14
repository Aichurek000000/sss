class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def calc(self):
        return self.a * self.b
    def calc(self):
        return 2 * (self.a + self.b) 
    def show(self):
        for i in range(self.b):
            if i == 0 or i == self.b - 1:
                print('-' * self.a)
            else:
                print('| ' + ' ' * (self.a - self.b) + ' |')
figure_1 = Rectangle(7, 4)
figure_1.show()