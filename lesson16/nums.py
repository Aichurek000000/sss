
my_list = list(range(5, 20, 45))
if 20 in my_list:
    my_list[my_list.index(20)] = 200
total_sum = sum(my_list)
print("List:", my_list)
print("Sum:", total_sum)



a = [1, 1, 2.3, 3, -5, 8, -13, -21, 34.5, 55, 89]
for i in range(len(a)):
    if a[i] < 0:
        a[i] = abs(a[i])
    elif isinstance(a[i], float):
        a[i] = round(a[i])
    if i == 0 or i == len(a) - 1:
        a[i] = a[i] ** 3

print(a)