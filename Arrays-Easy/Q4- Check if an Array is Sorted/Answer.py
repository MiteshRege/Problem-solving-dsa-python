# Approach 1 :
# Complexity Analysis:
# Time Complexity: O(n^2) as we are using two nested loops.


def isSorted_app_1(arr, n):
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                return False

    return True


# Approach 2 : Using Sorting
# Complexity Analysis:
# Time Complexity: O(n log n) due to the sorting operation.


def isSorted_app_2(arr):
    a = arr.copy()
    a.sort()
    if a == arr:
        return True
    return False


# Approach 3 : Single Pass
# Complexity Analysis:
# Time Complexity: O(n) as we traverse the array only once.


def isSorted(arr, n):
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return False
    return True


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [5, 3, 4, 1, 2]

    print(
        "Is array sorted (Approach 1)? :", isSorted_app_1(arr1, len(arr1))
    )  # Output: True
    print(
        "Is array sorted (Approach 1)? :", isSorted_app_1(arr2, len(arr2))
    )  # Output: False

    print("Is array sorted (Approach 2)? :", isSorted_app_2(arr1))
    # Output: True

    print("Is array sorted (Approach 2)? :", isSorted_app_2(arr2))
    # Output: False

    print("Is array sorted (Approach 3)? :", isSorted(arr1, len(arr1)))
    # Output: True

    print("Is array sorted (Approach 3)? :", isSorted(arr2, len(arr2)))
    # Output: False
