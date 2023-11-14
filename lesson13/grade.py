grades1 = int(input("Enter a point: "))
grades2 = int(input("Enter a point: "))
grades3 = int(input("Enter a point: "))
grades4 = int(input("Enter a point: "))
grades5 = int(input("Enter a point: "))

def calculate_average(*grades):
    total = sum(grades)
    average = total / len(grades)
    return average

average = calculate_average(grades1, grades2, grades3, grades4, grades5)
print(average)