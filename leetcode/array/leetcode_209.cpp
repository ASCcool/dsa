// Problem statement: https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=study-plan-v2&envId=top-interview-150
// (Minimum Size Subarray Sum) -- Sliding window approach

class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int l = 0, curr = 0, minSize = INT_MAX;

        for (int r = 0; r < nums.size(); r++) {
            curr += nums[r]; // Expand the window by adding nums[r]

            while (curr >= target) { // Contract the window
                minSize = min(minSize, r - l + 1);
                curr -= nums[l]; // Shrink from the left
                l++;
            }
        }

        return (minSize == INT_MAX) ? 0 : minSize;
    }
};