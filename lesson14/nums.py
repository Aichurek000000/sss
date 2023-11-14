num = [5, 3, 7]
res = [nums ** 2 for nums in num]
res_dict = {num: num ** 3 for num in num}
info = {"address": "Isanova", "floor": 7, "has_parking": True}
converted = [info[key] for key in info]
print(converted)
nums_1 = [num + 1 for num in nums]
nums_2 = [num + 1 for num in nums if num >=5]