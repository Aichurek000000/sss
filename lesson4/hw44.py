num = input("Enter 4 digit numbers: ")
hundreds = int(num[0])
tens = int(num[1])
digits = int(num[2])
four = int(num[3])
sum = hundreds + tens + digits + four
mult = hundreds * tens * digits + four
print(sum)
print(mult)