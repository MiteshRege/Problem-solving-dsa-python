# Maximum Sum of Any Subarray of Size K
# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.
# Example:
# Input: [1, 5, 4, 2, 9, 9, 9], k=3
# Output: 27

# Sliding Window Approach
# Time Complexity: O(N)
# Space Complexity: O(1)
# code:

def max_sum_subarray_of_size_k(arr, k):
    start = 0
    local_sum = 0
    global_sum = float('-inf')

    for end in range(len(arr)):
        local_sum += arr[end]  # expand window

        # when window size exceeds k, shrink it
        if end - start + 1 > k:
            local_sum -= arr[start]
            start += 1

        # when window size == k, update answer
        if end - start + 1 == k:
            global_sum = max(global_sum, local_sum)

    return global_sum

# Example usage:
if __name__ == "__main__":
    arr = [1, 5, 4, 2, 9, 9, 9]
    k = 3
    result = max_sum_subarray_of_size_k(arr, k)
    print(f"The maximum sum of any contiguous subarray of size {k} is: {result}")
