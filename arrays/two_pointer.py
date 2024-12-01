"""
Two pointer problems are usually O(n) algorithms, except 3Sum problem variations
Some common problems that can be solved with two pointer -

1. Check if a string/array of chars is a palindrome
2. Reverse an array in-place
3. Given a target, find elements (a pair) that sum up to a target ==> 3 sum variation

Some variations around two pointers is discussed below
"""

# Given an unsorted array, move all zeros to the left/right ==> nums[i] == 0 or nums[i] != 0
def moveZerosToStart(nums):
    n = len(nums)
    j = 0  # Pointer for the next zero position

    for i in range(n):
        if nums[i] == 0:  # If the element is zero
            # Swap the elements at i and j
            nums[i], nums[j] = nums[j], nums[i]
            j += 1  # Move the pointer for zeros
    
    return nums

# Given a sorted array, find a pair that sums up to a target
def twoSum(nums, target):
    i, j = 0, len(nums)-1
    while i < j:
        curr_sum = nums[i] + nums[j]
        print(curr_sum, target)
        if curr_sum < target:
            i += 1
        elif curr_sum > target:
            j -= 1
        else:
            print(f"Found indices {i} and {j} such that nums[i]+nums[j]={target}")
            return i, j
    print("No pairs found")
    return -1, -1

# This has to be an O(n^2) algorithm due to its inherent complexity
# Given a sorted array, find a triplet that sums up to a target
def threeSum(nums, target):
    for k in range(len(nums)):
        i, j, modified_target = k+1, len(nums)-1, target-nums[k]
        while i < j:
            curr_sum = nums[i] + nums[j]
            print(curr_sum, modified_target)
            if curr_sum < modified_target:
                i += 1
            elif curr_sum > modified_target:
                j -= 1
            else:
                # k will always be shortest of all three
                print(f"Found indices {k}, {i} and {j} such that nums[i]+nums[j]+nums[k]={target}")
                return k, i, j
    print("No pairs found")
    return -1, -1, -1


if __name__ == "__main__":
    # Example Usage:
    arr = [0, 1, 0, 3, 12]
    print(moveZerosToStart(arr))  # Output: [0, 0, 1, 3, 12]
    arr = [0, 0, 1, 3, 12]
    print(twoSum(arr, 13)) # Output: 2, 4
    print(threeSum(arr, 16)) # Output: 2, 3, 4