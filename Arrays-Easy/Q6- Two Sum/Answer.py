# Two Sum Probelm

# Approach 1 : Brute Force
# Complexity Analysis:
# Time Complexity: O(n^2) as we have nested loops.
# Space Complexity: O(1) as we are not using any extra space.


# Code:
def twoSum_app_1(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []  # Return empty list if no solution found


# Approach 2 : Using Hash Map
# Complexity Analysis:
# Time Complexity: O(n) as we traverse the array once.
# Space Complexity: O(n) for the hash map.

# Code:


def twoSum_app_2(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []  # Return empty list if no solution found


# Approach 3 : Two Pointers (Only works if the array is sorted)
# Complexity Analysis:
# Time Complexity: O(n) as we traverse the array once.
# Space Complexity: O(1) as we are not using any extra space.

# Code:


def twoSum_app_3(nums, target):
    nums_with_indices = [(num, i) for i, num in enumerate(nums)]
    nums_with_indices.sort()  # Sort based on the numbers

    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums_with_indices[left][0] + nums_with_indices[right][0]
        if current_sum == target:
            return [nums_with_indices[left][1], nums_with_indices[right][1]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []  # Return empty list if no solution found


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print("Two Sum (Approach 1):",
          twoSum_app_1(nums, target)
          )  # Output: [0, 1]

    print("Two Sum (Approach 2):",
          twoSum_app_2(nums, target)
          )  # Output: [0, 1]

    print("Two Sum (Approach 3):",
          twoSum_app_3(nums, target)
          )  # Output: [0, 1]
    # Note:
    # Approach 3 assumes the input array is sorted.
    # If not, it sorts a copy of the array with indices.
