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

# Problem statement: https://leetcode.com/problems/minimum-window-substring/description/

from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""
        
        # Count the frequency of characters in t
        t_freq = Counter(t)
        window_freq = {}
        
        # Variables to track the state of the window
        have, need = 0, len(t_freq)
        left = 0
        min_len = float("inf")
        res = ""
        
        # Expand the window by moving the right pointer
        for right in range(len(s)):
            char = s[right]
            window_freq[char] = window_freq.get(char, 0) + 1
            
            # If the character is in t and its count matches t_freq
            if char in t_freq and window_freq[char] == t_freq[char]:
                have += 1
            
            # Contract the window until it's no longer valid
            while have == need:
                # Update the result if the current window is smaller
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    res = s[left:right + 1]
                
                # Remove the leftmost character from the window
                window_freq[s[left]] -= 1
                if s[left] in t_freq and window_freq[s[left]] < t_freq[s[left]]:
                    have -= 1
                left += 1
        
        return res