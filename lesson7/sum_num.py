num = [1, 3, 5, 5, 3.4]
s = 0
for n in num:
    if isinstance (n, (int, float)):
        s += n
print(s)