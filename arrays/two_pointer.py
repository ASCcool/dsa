"""
Two pointer problems are usually O(n) algorithms, except 3Sum problem variations
Some common problems that can be solved with two pointer -

1. Check if a string/array of chars is a palindrome: https://leetcode.com/problems/valid-palindrome/submissions/1478835793/
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

# Given an array of 0s, 1s and 2s, sort it such that 0s, then 1s and then 2s appear left to right
# Input [2,1,1,0,0] ==> Output [0,0,1,1,2]
def ternary_separator(colors):
    current, start, end = 0, 0, len(colors)-1
    # start tracks 0, current tracks 1, end tracks 2
    while current <= end:
      if colors[current] == 0:
        # swap current with start and increment both
        colors[current], colors[start] = colors[start], colors[current]
        start += 1
        current += 1
      elif colors[current] == 1:
        # no need to swap 1, it takes care of itself
        current += 1
      else:
        colors[current], colors[end] = colors[end], colors[current]
        end -= 1
    return colors

def twoSumWithoutSorting(self, nums: List[int], target: int) -> List[int]:
    i, n = 0, len(nums)
    mp = {}
    while i < n:
        find = target - nums[i]
        if find in mp:
            return [min(i, mp[find]), max(i, mp[find])]
        else:
            mp[nums[i]] = i
            i += 1
    return [-1, -1]

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
# Leetcode link: https://leetcode.com/problems/3sum/
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