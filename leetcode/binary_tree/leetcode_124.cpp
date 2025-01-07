// Problem statement - https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
/*
Idea is to iterate down the tree and calculate local path sum as well as propagate the max sum including current node to the caller, and update glocal max wherever applicable
Suppose tree is this, the optimal path is 15 -> 20 -> 7 yielding 42 but if you talk about node 20, it's caller (right of -10)
will be returned max(20's left, 20's right)+20 = 35 and left path of -10 will return 9
this will effectively mean that including -10, you will have chosen the path 9 -> -10 -> 20 -> 15 = 41 < 42
        -10
       /  \
      9    20
          /  \
         15   7
*/

class Solution {
private:
    int maxSum = INT_MIN;
public:
    int maxPathSum(TreeNode* root) {
        calculatemaxPathSum(root);
        return maxSum;
    }
    int calculatemaxPathSum(TreeNode* root) {
        if (!root) {
            return 0;
        }
        // calculate the max sum across all paths including the left child node
        int left = max(calculatemaxPathSum(root->left),0);
        // calculate the max sum across all paths including the right child node
        int right = max(calculatemaxPathSum(root->right),0);
        // find current path sum
        int currSum = left+right+root->val;
        // update global max if aaplicable
        maxSum = max(maxSum, currSum);
        // return current max till current node (i.e. starting at current node, which subtree you should go to)
        return max(left,right)+root->val;
    }
};