def recursive_search(lst, target):
    if not lst:
        return -1
    if lst[0] == target:
        return 0
    ind = recursive_search(lst[1:], target)
    if ind == -1:
        return -1
    return ind + 1

lst = [1, 2, 3, 4, 5, 6, 7]
target = 4
result = recursive_search(lst, target)
print(result)