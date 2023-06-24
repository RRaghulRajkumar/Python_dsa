def plusOne(digits):
    n = len(digits)
    
    # Start from the least significant digit
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
    
    # If all digits were 9, add an additional digit at the beginning
    return [1] + digits
digits = [1, 2, 3]
result = plusOne(digits)
print(result)  # Output: [1, 2, 4]
