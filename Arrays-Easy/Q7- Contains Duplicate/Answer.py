# Contains Duplicate

# Brute Force Approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# code


def containsDuplicate_approach_1(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False

# Optimal Approach using HashSet
# Time Complexity: O(n)
# Space Complexity: O(n)
# code


def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Example usage:


nums = [1, 2, 3, 1]
print(containsDuplicate_approach_1(nums))  # Output: True
print(containsDuplicate(nums))  # Output: True
