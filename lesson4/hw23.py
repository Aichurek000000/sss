number = int(input("Enter a number: "))
if 100 <= number <= 999:
    hundred = number // 100
    hundred1 =   number % 100
    ten = number // 10
    ten1 = number % 10
    sum = hundred1 + hundred + ten1 + ten 
    digit = hundred1 + hundred + ten1 + ten
    print("sum is: ", sum)
    print("digit: " , digit)
else:
    print("It's not a digit numbers.")