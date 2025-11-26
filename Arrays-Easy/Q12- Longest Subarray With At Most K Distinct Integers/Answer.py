
# Longest Subarray With At Most K Distinct Integers

def longest_subarray_at_most_k(arr, k):
    count_map = {}
    start = 0
    max_length = 0

    for end in range(len(arr)):
        count_map[arr[end]] = count_map.get(arr[end], 0) + 1

        while len(count_map) > k:
            count_map[arr[start]] -= 1
            if count_map[arr[start]] == 0:
                del count_map[arr[start]]
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length


# Example usage:
arr = [1, 2, 1, 2, 3]
k = 2
print(longest_subarray_at_most_k(arr, k))  # Output: 4        
        