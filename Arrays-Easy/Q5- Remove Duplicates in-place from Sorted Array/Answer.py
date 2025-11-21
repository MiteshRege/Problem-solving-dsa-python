# Approach 1 : Using a Set
# Complexity Analysis:
# Time Complexity: O(n) as we traverse the array once.
# Space Complexity: O(n) in the worst case when there are no duplicates.
# but this we cant consider as in-place.
# -> IGNORE in interview just let them know, we can do better.


# Code:
def removeDuplicates_app_1(nums):
    seen = set()
    write_index = 0

    for num in nums:
        if num not in seen:
            seen.add(num)
            nums[write_index] = num
            write_index += 1
    return write_index  # Length of array without duplicates


# Approach 2 : Two Pointers
# Complexity Analysis:
# Time Complexity: O(n) as we traverse the array once.
# Space Complexity: O(1) as we are not using any extra space.
# Remmember :
# The array is sorted and want inplace solution then use two pointer approach.
# Code:


def removeDuplicates_app_2(nums):
    if not nums:
        return 0

    slow_pt = 1

    for fast_pt in range(1, len(nums)):
        if nums[fast_pt] != nums[fast_pt - 1]:
            nums[slow_pt] = nums[fast_pt]
            slow_pt += 1
    return slow_pt  # Length of array without duplicates


if __name__ == "__main__":
    arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    length = removeDuplicates_app_2(arr)
    print("Length of array after removing duplicates:", length)
    print("Array after removing duplicates:", arr[:length])

# alternate code for approach 2:
# a = [1,1,2,2,2,3,3]
# n = len(a)
# if n<2:
#     print(a)
#     # break
# i = 0
# j =1
# while j<=n-1:
#     if a[i]!=a[j]:
#         i+=1
#         a[i]=a[j]
#         j+=1
#     else:
#         j+=1
# ans = i
# for x in range(i+1,n):
#     a[x] = _
# return ans+!
# or asked return a
