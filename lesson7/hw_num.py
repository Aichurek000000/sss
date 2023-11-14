nums = [6, 2, 88, 23, 0, -5, 30, 9, 20, 10, 6, 56, -7] 
tree = [] 
five = []

for num in nums:
     if num == 0:
          continue
     if num % 3 == 0: tree.append(num)
     if num % 5 == 0: five.append(num)

print(tree) 
print(five)