num_1 = int(input("Enter a num: "))
num_2 = int(input("Enter a num: "))
operation = input("Enter an operator: ")
if operation == "+":
    result = num_1 + num_2
elif operation == "-":
    result = num_1 - num_2
elif operation == "*":
    result = num_1 * num_2
elif operation == "/":
    result = num_1 / num_2
else:
    result = "no"
print(result)

