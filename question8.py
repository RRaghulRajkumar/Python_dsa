def findErrorNums(nums):
    n = len(nums)
    num_set = set()
    duplicate = -1

    # Find the duplicate number
    for num in nums:
        if num in num_set:
            duplicate = num
        else:
            num_set.add(num)

    # Find the missing number
    missing = -1
    for i in range(1, n + 1):
        if i not in num_set:
            missing = i
            break

    return [duplicate, missing]
nums = [1, 2, 2, 4]
result = findErrorNums(nums)
print(result)  # Output: [2, 3]
