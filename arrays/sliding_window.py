# Longest Substring Without Repeating Characters
# Leetcode link - https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    """
    Use a sliding window approach, eliminate from the left of the window 
    if you find the rightmost character in the current window and set
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            print(l, r)
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res