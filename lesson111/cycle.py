enter = int(input("Enter a number: "))
i = 1
while i <= enter:
    print(i, end=" ")
    i += 3
for j in range(1, enter + 1, 4):
    print(j, end=" ")