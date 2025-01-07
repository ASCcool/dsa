// Problem: https://leetcode.com/problems/sum-root-to-leaf-numbers/

class Solution {
public:
    int sumNumbers(TreeNode* root) {
        return dfs(root, 0);
    }
    
    int dfs(TreeNode* node, int currentSum) {
        if (!node) return 0; // Base case: null node
        
        // Update the current sum for this path
        currentSum = currentSum * 10 + node->val;
        
        // If it's a leaf node, return the current sum
        if (!node->left && !node->right) {
            return currentSum;
        }
        
        // Recurse on left and right subtrees
        return dfs(node->left, currentSum) + dfs(node->right, currentSum);
    }
};