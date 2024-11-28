def find_max_min(nums):
    maxs = max(nums)
    mins = min(nums)
    return maxs, mins


nums = [13, 346, 34576, 457, 5, 8568, 56, 8568, 14, 23, 44, 2345]
max_value, min_value = find_max_min(nums)
print(max_value)
print(min_value)
