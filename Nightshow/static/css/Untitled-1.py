def min_operations_to_zero(arr):
    # Calculate the XOR of the entire array
    total_xor = 0
    for num in arr:
        total_xor ^= num
        print(total_xor)
    # If the total XOR is already zero, we can make all elements zero in one operation
    if total_xor == 0:
        return 1
    
    # If total XOR is not zero, we try to split the array into segments where each segment has XOR = total_xor
    current_xor = 0
    segments = 0
    for num in arr:
        current_xor ^= num
        # When we reach a segment with XOR equal to total_xor, we reset the current_xor and increase segment count
        if current_xor == total_xor:
            segments += 1
            current_xor = 0
    
    # If we can split into at least two segments with XOR equal to total_xor, we need two operations
    if segments >= 2:
        return 2
    else:
        # Otherwise, it's not possible to make all elements zero
        return -1

# Sample Input for Testing
n = 5
arr = [0, 2, 3, 0, 2]

# Function call and output
print(min_operations_to_zero(arr))  # Expected output: 2