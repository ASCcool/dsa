// Leetcode link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1495392126/
// Find min till now and subtract it from current element to find profit and store max in this manner
// Buy one day and sell one day
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProfit = 0, currProfit = 0, minBuy = INT_MAX;
        for (int i = 0; i < prices.size(); ++i) {
            // Update minimum buy price
            if (prices[i] < minBuy) {
                minBuy = prices[i];
            }
            // Calculate current profit
            currProfit = prices[i] - minBuy;
            maxProfit = currProfit > maxProfit ? currProfit : maxProfit;
        }
        return maxProfit;
    }
};
