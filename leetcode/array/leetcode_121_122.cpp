// Problem link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

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

// Problem link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min=INT_MAX,profit=0,total=0;
        for (int price:prices) {
            if (price<min) {
                min=price;
            }
            profit = price-min;
            if (profit>0) {
                total += profit;
                // only difference here is that since you can buy again on same day, set min to current price as buy for future sale
                min=price;
            }
        }
        return total;
    }
};