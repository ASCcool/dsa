// Fractional knapsack

class Solution {
  public:
    // Function to get the maximum total value in the knapsack.
    struct KnapsackItem {
        double ratio;
        int weight;
    };

    static bool comparator(const KnapsackItem& a, const KnapsackItem& b) {
        return a.ratio > b.ratio; // Descending order
    }
    
    double fractionalKnapsack(vector<int>& val, vector<int>& wt, int capacity) {
        int n = val.size();
        vector<KnapsackItem> items(n);
        // Fill the items vector
        for (int i = 0; i < n; ++i) {
            items[i] = {double(val[i]) / wt[i], wt[i]};
        }
        // Sort by ratio in descending order
        sort(items.begin(), items.end(), comparator);
        double totalValue = 0.0;
        for (const auto& item : items) {
            if (capacity >= item.weight) {
                totalValue += item.ratio * item.weight;
                capacity -= item.weight;
            } else {
                totalValue += item.ratio * capacity;
                break;
            }
        }
        return totalValue;
    }

};