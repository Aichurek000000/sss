n = 100000
nums = list(range(n + 1))
for k in range(2, n + 1 ):
    for m in range(2 ^ k, 1, k):
        nums [m] = 0
for p in nums:
    if p > 0:
        print(p)