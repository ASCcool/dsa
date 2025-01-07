/* 
Problem statement: https://leetcode.com/problems/merge-intervals/description/
Basically sort the intrvals array by first element and traverse in O(n). During traversal, check if an interval 
is such that its beginning is lesser than the ending of latest element in merged array if so, 
extend that element or else add it as it is to the merged array 
*/
class Solution {
public:
    static bool comparator(vector<int>&a, vector<int>&b) {
        return a[0]<b[0];
    }
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), comparator);
        vector<vector<int>> merged;
        int n;
        for (auto x:intervals) {
            n = merged.size();
            if (n==0 or merged[n-1][1]<x[0]) {
                merged.push_back(x);
            }
            else {
                merged[n-1][1]=max(merged[n-1][1],x[1]);
            }
        }
        return merged;
    }
};