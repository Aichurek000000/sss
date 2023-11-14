num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

def sum_pow(num1, num2):
    result = num1 ** num2
    digit = sum(int(digit) for digit in str(result))
    return digit

result = sum_pow(num1, num2)
print(result)