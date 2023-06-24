def twoSum(nums, target):
    num_dict = {}  # Dictionary to store the complement of each number
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # If the complement is already in the dictionary, we found the solution
        if complement in num_dict:
            return [num_dict[complement], i]
        
        # Otherwise, store the current number and its index in the dictionary
        num_dict[num] = i
    
    # If no solution is found, return an empty list or raise an exception
    return []
nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)  # Output: [0, 1]
