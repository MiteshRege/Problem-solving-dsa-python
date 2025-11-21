# Solution1: Sorting
# Complexity Analysis:
# Time Complexity: O(n log n) due to the sorting operation.
# Code:
from typing import List


def sortArr(arr: List[int]) -> int:
    arr.sort()
    return arr[-1]


# Solution 2: Linear Scan
# Complexity Analysis:
# Time Complexity: O(n) as we traverse the array only once.
# Code:


def largestElement(arr: List[int]) -> int:
    max_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
    return max_element


if __name__ == "__main__":
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print("Largest element using sorting:", sortArr(arr))
    print("Largest element using linear scan:", largestElement(arr))
