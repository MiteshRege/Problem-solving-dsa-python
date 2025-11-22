# Longest Subarray With All Distinct Elements
# Given an array of integers, find the length of the longest subarray that contains all distinct
# Time Complexity: O(N)
# Space Complexity: O(N)

# code:
def longest_distinct_subarray(arr):
    start = 0
    seen = set()
    global_subarr_len = 0

    for end in range(len(arr)):
        if arr[end] not in seen:
            seen.add(arr[end])
        else:
            while arr[end] in seen:
                seen.remove(arr[start])
                start += 1
            seen.add(arr[end])

        global_subarr_len = max(global_subarr_len, end - start + 1)

    return global_subarr_len

# Example usage:
if __name__ == "__main__":
    arr = [5, 1, 3, 5, 2, 3, 4, 1]
    result = longest_distinct_subarray(arr)
    print("Length of the longest subarray with all distinct elements:", result)  # Output: 5

# # Remmember this:
# for end in array:
#     while duplicate:
#         shrink window from start
#     add element
#     update longest window
