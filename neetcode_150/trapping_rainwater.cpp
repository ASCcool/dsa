// Problem: https://neetcode.io/problems/trapping-rain-water

/* 
Approach is this - 
1. Find prefix and suffix maximum elements for an array (this is not the same as NGE or NSE as you see the global max rather than immediate max)
2. For water to be trapped at any position, that position has to be bounded, i.e. prefix and suffix maxes must exist)
3. water[i] = min(prefixMax[i],suffixMax[i])-height[i] (elevation is height[i] so subtract it)
4. add all waters
*/

class Solution {
public:
    vector<int> prefixSuffixMax(vector<int>& height, string traversal="right") {
        int n = height.size();
        vector<int> maxArray(n, -1);
        int currMax = -1;
        if (traversal == "right") {
            // Traverse from right to left
            for (int i = n - 1; i >= 0; --i) {
                currMax = max(currMax, height[i]);
                maxArray[i] = currMax;
            }
        } else {
            // Traverse from left to right
            for (int i = 0; i < n; ++i) {
                currMax = max(currMax, height[i]);
                maxArray[i] = currMax;
            }
        }
        return maxArray;
    }
    int trap(vector<int>& height) {
        vector<int> prefixMax, suffixMax;
        prefixMax = prefixSuffixMax(height, "left");
        suffixMax = prefixSuffixMax(height, "right");
        int total = 0;
        for (int i=0;i<height.size();++i) {
            if (prefixMax[i]!=-1 && suffixMax[i]!=-1) {
                total += min(prefixMax[i],suffixMax[i])-height[i];
            }
        }
        return total;
    }
};
