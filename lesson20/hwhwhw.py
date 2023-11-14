class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def get_string(self):
        self.input_string = input("Enter a word: ")

    def print_string(self):
        print(self.input_string.upper())
        
str_manipulator = StringManipulator()
str_manipulator.get_string() 
str_manipulator.print_string()  