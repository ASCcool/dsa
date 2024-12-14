# Problem: https://leetcode.com/problems/continuous-subarrays/description/ 
# Solution: https://youtu.be/SWyGD8w_85E?si=rWD21OMRhuY81Q77

from sortedcontainers import SortedDict

def continuousSubarrays(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i, j, count, n = 0, 0, 0, len(nums)
    mp = SortedDict()
    while j < n:
        # Safely increment the value for nums[j]
        mp[nums[j]] = mp.get(nums[j], 0) + 1
        # Shrink the window if the difference between max and min exceeds 2
        while max(mp) - min(mp) > 2:
            mp[nums[i]] -= 1
            if mp[nums[i]] == 0:
                del mp[nums[i]]
            i += 1
        # Count the valid subarrays ==> length of the current valid subarray window
        count += j - i + 1
        j += 1
    return count

if __name__ == "__main__":

    # answer is 8 continuous subarrays ==> {5}, {5,4}, {4}, {4,2}, {2}, {2}, {2,4}, {4,2,4}
    continuousSubarrays([5,4,2,4])