def longest_consecutive_sequence(nums):
    set1 = set(nums)
    max_length = 0

    for num in set1:
        if num - 1 in set1:
            current_num = num
            current_num = 1

        while current_num + 1 in num_set:
            current_num += 1
            max_length += 1

        max(max_length, current_num)

    return max_length


print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))

"""
    EXPECTED OUTPUT:
    ----------------
    4

"""