a = int(input("Enter your grade: "))
b = int(input("Enter your done hw: "))
if a >= 90 and b >= 10:
    print("Great!")
elif a >= 70 or b >= 5:
    print("Good job!")
else:
    print("The assessment is satisfactory.")