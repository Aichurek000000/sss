name = input()
age = int(input())

in_ten = age + 10
str_age = str(in_ten)

res_1 = "Вас зовут " + name + ", через 10 лет вам будет " + str_age
print(res_1)

# res_2 = f"Вас зовут {name}, через 10 лет вам будет {str_age}"
res_2 = f"Вас зовут {name}, через 10 лет вам будет {age + 10}"
print(res_2)