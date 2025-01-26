/*

// Problem statement: https://leetcode.com/problems/candy/description/?envType=study-plan-v2&envId=top-interview-150

// Input:
ratings = {1, 3, 2, 1};

// Output:
Candies vector after forward pass: {1, 2, 1, 1}
Candies vector after backward pass: {1, 3, 2, 1}
Total candies: 1 + 3 + 2 + 1 = 7

*/

class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();
        vector<int> candies(n, 1); // Start with 1 candy for each child
        // Forward pass
        for (int i = 1; i < n; i++) {
            if (ratings[i] > ratings[i - 1]) {
                candies[i] = candies[i - 1] + 1;
            }
        }
        // Backward pass to take care of both forward and backward pass max values
        for (int i = n - 2; i >= 0; i--) {
            if (ratings[i] > ratings[i + 1]) {
                candies[i] = max(candies[i], candies[i + 1] + 1);
            }
        }
        // Total candies needed
        return accumulate(candies.begin(), candies.end(), 0);
    }
};