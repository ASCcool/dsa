// Problem statement: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
// Greedy + Binary search on range (like max tastiness)
class Solution {
public:
    bool canShip(vector<int>& weights, int checkWeight, int days) {
        int total=1, capacity=0;
        for (int w:weights) {
            if (capacity+w<=checkWeight) {
                capacity+=w;
            }
            else {
                capacity=w;
                total+=1;
                if (total>days) return false;
            }
        }
        return true;
    }
    int shipWithinDays(vector<int>& weights, int days) {
        int low=INT_MIN,mid=0,high=0;
        for (int w:weights) {
            if (w>low) low=w;
            high+=w;
        }
        // min weight of behicle must be max of the weights array and max weight can be sum of all
        while (low < high) {
            mid = (low+high)/2;
            if (canShip(weights, mid, days)) {
                high = mid; // Try a smaller capacity
            } else {
                low = mid + 1; // Increase capacity
            }
        }
        // The minimum capacity
        return low; 
    }
};