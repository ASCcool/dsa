// Problem statement: https://leetcode.com/problems/max-chunks-to-make-sorted-ii/description/
// Chalo DSA first round
/**
 * Problem: Max Chunks To Make Sorted II
 *
 * Given an unsorted array, determine the maximum number of chunks (subarrays)
 * into which the array can be partitioned such that sorting each chunk and
 * concatenating them results in a sorted array.
 *
 * Approaches:
 * 1. Prefix Sum Approach (Full-proof, handles cases where there are duplicate elements in the array)
 * 2. Max-So-Far Approach (Initial broad case solution, basic thinking)
 */

class Solution {
public:
    /**
     * Prefix Sum Approach:
     * - Compare the cumulative sum of the original array and its sorted version.
     * - If the prefix sums match at any index, it guarantees all elements up to
     *   that point can form a valid chunk.
     *
     * Why it works:
     * - Matching prefix sums ensure the elements and their frequencies match in
     *   the two arrays, making the partition valid.
     *
     * Time Complexity: O(n log n) due to sorting.
     * Space Complexity: O(n) for storing the sorted array.
     */
    int maxChunksToSortedPrefixSum(vector<int>& arr) {
        vector<int> sorted_arr = arr;
        sort(sorted_arr.begin(), sorted_arr.end());

        int chunks = 0;
        long long prefix_sum_original = 0, prefix_sum_sorted = 0;

        for (int i = 0; i < arr.size(); ++i) {
            prefix_sum_original += arr[i];
            prefix_sum_sorted += sorted_arr[i];

            // If prefix sums match, it's a valid chunk boundary
            if (prefix_sum_original == prefix_sum_sorted) {
                ++chunks;
            }
        }

        return chunks;
    }

    /**
     * Max-So-Far Approach:
     * - Track the maximum value seen so far in the original array.
     * - Compare it to the corresponding value in the sorted array.
     * - If they match, it indicates a valid chunk boundary.
     *
     * Why it works:
     * - If the maximum value seen so far equals the maximum value in the sorted
     *   array up to the same point, the partition is valid.
     *
     * Limitations:
     * - Fails for arrays with duplicate values because it doesn't account for
     *   frequency matching.
     *
     * Time Complexity: O(n log n) due to sorting.
     * Space Complexity: O(n) for storing the sorted array.
     */
    int maxChunksToSortedMaxSoFar(vector<int>& arr) {
        vector<int> sorted_arr = arr;
        sort(sorted_arr.begin(), sorted_arr.end());

        int max_so_far = INT_MIN;
        int chunks = 0;

        for (int i = 0; i < arr.size(); ++i) {
            max_so_far = max(max_so_far, arr[i]);

            // If max_so_far matches the value in sorted_arr, it's a valid chunk boundary
            if (max_so_far == sorted_arr[i]) {
                ++chunks;
            }
        }

        return chunks;
    }
};