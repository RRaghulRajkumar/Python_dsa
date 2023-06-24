def removeElement(nums, val):
    k = 0  # Variable to count the number of elements not equal to val
    
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    
    return k
nums = [3, 2, 2, 3]
val = 3
k = removeElement(nums, val)
print("k =", k)  # Output: 2
print("nums =", nums[:k] + ["_*"] * (len(nums) - k))  # Output: [2, 2, '_*', '_*']
