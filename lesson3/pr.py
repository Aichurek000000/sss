a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a > c and a > b and a > d:
    print(a)
elif b > c and b > a and b > d:
    print(b)
elif c > a and c > b and c > d:
    print(c)
else:
    print(d)
