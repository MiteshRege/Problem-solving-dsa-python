# Longest Subarray With Sum ≤ K
# Problem Statement: Given an array of positive integers and a positive integer K, find the length of the longest subarray whose sum is less than or equal to K.
# Time Complexity: O(N)
# Space Complexity: O(1)

# code:
def longest_subarray_with_sum_at_most_k(arr, k):
    start = 0
    _sum = 0
    global_len = 0
    
    for end in range(len(arr)):
        _sum += arr[end]

        while _sum > k:
            _sum -= arr[start]
            start += 1
        
        global_len = max(global_len, end - start + 1)
    
    return global_len

# Example usage:
arr = [1, 2, 3, 4, 5]
k = 9
result = longest_subarray_with_sum_at_most_k(arr, k)
print("Length of the longest subarray with sum ≤ K:", result)  # Output: 3 (subarray [2, 3, 4])
# Test cases
assert longest_subarray_with_sum_at_most_k([1, 2, 3, 4, 5], 9) == 3  # subarray [2, 3, 4]
assert longest_subarray_with_sum_at_most_k([5, 1, 2, 3, 4], 8) == 3  # subarray [1, 2, 3]
assert longest_subarray_with_sum_at_most_k([2, 2, 2, 2], 5) == 2  # subarray [2, 2]
assert longest_subarray_with_sum_at_most_k([10, 20, 30], 15) == 0  # no valid subarray
assert longest_subarray_with_sum_at_most_k([], 10) == 0  # empty array
    