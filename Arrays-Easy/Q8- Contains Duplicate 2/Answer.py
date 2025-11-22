# Contins Duplicate 2
# Brute Force Approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)


def containsNearbyDuplicate_approach_1(nums, k):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j] and abs(i - j) <= k:
                return True
    return False

# Optimal Approach using HashMap
# Time Complexity: O(n)
# Space Complexity: O(n)


def containsNearbyDuplicate(nums, k):
    index_map = {}
    for i, num in enumerate(nums):
        if num in index_map and abs(i - index_map[num]) <= k:
            return True
        index_map[num] = i
    return False


# Sliding Window Approach using HashSet
# Time Complexity: O(n)
# Space Complexity: O(min(n, k))


def containsNearbyDuplicate_approach_3(nums, k):
    seen = set()
    for i in range(len(nums)):
        if nums[i] in seen:
            return True
        seen.add(nums[i])
        if len(seen) > k:
            seen.remove(nums[i - k])
    return False


# Example usage:


nums = [1, 2, 3, 1]
k = 3
print(containsNearbyDuplicate_approach_1(nums, k))  # Output: True
print(containsNearbyDuplicate(nums, k))  # Output: True
print(containsNearbyDuplicate_approach_3(nums, k))  # Output: True
