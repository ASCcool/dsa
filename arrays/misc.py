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


if __name__ == "__main__":
    nums = [3, 22, 1, 2, 9, 4, 5]
    print(longest_consecutive_subsequence(nums))  # 1, 2 are present
    print(longest_consecutive_sequence(nums))  # 1 to 5 all are present
