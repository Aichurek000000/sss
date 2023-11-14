num1 = int(input("Enter a num: "))
num2 = int(input("Enter a num: "))
num3 = int(input("Enter a num: "))
def find_max(num1, num2, num3):
    max_num = max(num1, num2, num3)
    return max_num
result_max = find_max(num1, num2, num3)
print(result_max)