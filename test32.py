# def find_duplicates(nums):
#     duplicate = []
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i] == nums[j]:
#                 duplicate.append(nums[i])
#     return duplicate

def find_duplicates(nums):
    count_num = {}

    for i in nums:
        count_num[i] = count_num.get(i, 0) + 1

    duplicate = []

    for x, y in count_num.items():
        if y > 1:
            duplicate.append(x)
    return duplicate


print(find_duplicates([1, 2, 3, 4, 5]))
print(find_duplicates([1, 1, 2, 2, 3]))
print(find_duplicates([1, 1, 1, 1, 1]))
print(find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]))
print(find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]))
print(find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]))
print(find_duplicates([]))

"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""

