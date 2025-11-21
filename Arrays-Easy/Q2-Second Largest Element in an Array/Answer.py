# Approach 1: Single Pass with Two Variables
# Complexity Analysis:
# Time Complexity: O(n) as we traverse the array twice.
# Space Complexity: O(1) since we are using a constant amount of space.


def getElements_approach_1(arr, n):
    if n == 0 or n == 1:
        print(-1, -1)  # edge case when only one element is present in array
    small = float("inf")
    second_small = float("inf")
    large = float("-inf")
    second_large = float("-inf")
    for i in range(n):
        small = min(small, arr[i])
        large = max(large, arr[i])
    for i in range(n):
        if arr[i] < second_small and arr[i] != small:
            second_small = arr[i]
        if arr[i] > second_large and arr[i] != large:
            second_large = arr[i]
    print("Second smallest is", second_small)
    print("Second largest is", second_large)


# Approach 2: Optimized Single Pass
# Complexity Analysis:
# Time Complexity: O(n) as we traverse the array only once.
# Space Complexity: O(1) since we are using a constant amount of space.


def secondLargestElement_approach_2(self, nums):
    max_num = float("-inf")
    max_second_num = float("-inf")
    for i in nums:
        if i > max_num:
            max_second_num = max_num
            max_num = i
        else:
            if i > max_second_num and i < max_num:
                max_second_num = i
    return max_second_num if max_second_num != float("-inf") else -1


if __name__ == "__main__":
    nums1 = [3, 5, 2, 9, 7]
    nums2 = [4, 4, 4, 4]
    print("Second largest using two pass approach:")
    print(getElements_approach_1(nums1, len(nums1)))
    print(getElements_approach_1(nums2, len(nums2)))
    print(
        "Second largest using optimized single pass:",
        secondLargestElement_approach_2(None, nums1),
    )  # Output: 7
    print(
        "Second largest using optimized single pass:",
        secondLargestElement_approach_2(None, nums2),
    )  # Output: -1
