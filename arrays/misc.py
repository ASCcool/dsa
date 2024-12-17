def longest_consecutive_subsequence(nums):
    """
    Sliding Window Approach to find the Longest Consecutive Subsequence:
    Given an unsorted list of integers, this function finds the length of the longest consecutive subsequence
    where consecutive elements have a difference of 1.

    Example:
    Input: [1, 2, 3, 5]
    Output: 3 (for the subsequence [1, 2, 3])
    """
    print(nums)
    l, r, n = 0, 1, len(nums)
    if n == 1:
        return 1
    longest = 0
    while l < n:
        local = 0
        while r < n-1 and nums[r] - nums[r-1] == 1:
            r += 1
            local += 1
        longest = max(longest, local+1)
        l, r = r, r+1
    return longest


def longest_consecutive_sequence(nums):
    """
    Set-Based Approach to find the Longest Consecutive Sequence:
    Given an unsorted list of integers, this function finds the length of the longest consecutive subsequence
    in linear time using a set for fast lookups.

    Example:
    Input: [1, 9, 3, 10, 4, 20, 2]
    Output: 4 (for the subsequence [1, 2, 3, 4])
    """
    if not nums:
        return 0

    # Create a set of numbers for O(1) lookups
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Check if it's the start of a sequence
        if num - 1 not in num_set:  # Start a new sequence if `num - 1` doesn't exist
            current_num = num
            current_streak = 1

            # Expand the sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            # Update the longest streak found
            longest = max(longest, current_streak)

    return longest


# Leetcode problem: https://leetcode.com/problems/maximum-tastiness-of-candy-basket/
# Binary search for "tasty" value and find if atleast k elements in the array satisfy 
# the min tastiness of "tasty". If found, store it else go for higher or lower value 
# of tasty accordingly. This is and O(n * log (n)) solution
class MaxTastinessOfBasket:
    def findKcandies(self, price, tasty, k):
        largest = 0
        count = 1
        for current in range(1, len(price)):
            if price[current] - price[largest] >= tasty:
                largest = current
                count += 1
        return count >= k
    def maximumTastiness(self, price, k):
        price.sort()  # Sort the prices in ascending order
        low, high = 0, price[-1] - price[0]
        tasty = 0
        # Binary search for the maximum tastiness
        while low <= high:
            mid = low + (high - low) // 2
            if self.findKcandies(price, mid, k):
                tasty = mid  # Update tastiness if the condition is satisfied
                low = mid + 1  # Try for a larger tastiness value
            else:
                high = mid - 1  # Try for a smaller tastiness value
        return tasty


if __name__ == "__main__":
    nums = [3, 22, 1, 2, 9, 4, 5]
    print(longest_consecutive_subsequence(nums))  # 1, 2 are present
    print(longest_consecutive_sequence(nums))  # 1 to 5 all are present
