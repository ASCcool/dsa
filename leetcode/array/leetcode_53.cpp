// Problem statement: https://leetcode.com/problems/maximum-subarray/description/
// Kdane algorithm

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int curr = 0, global = INT_MIN;
        for (int num : nums) {
            curr = max(num, curr + num); // Choose between starting fresh or continuing the current subarray
            global = max(global, curr); // Update the global maximum
        }
        return global;
    }
};