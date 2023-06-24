def moveZeroes(nums):
    j = 0  # Pointer to track the position for nonzero elements
    
    # Iterate through the array
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1
    
    # Fill the remaining positions with zeros
    while j < len(nums):
        nums[j] = 0
        j += 1
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
