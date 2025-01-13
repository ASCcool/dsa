// Problem statement: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

// Lowest Common Ancestor (LCA) of binary tree

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (!root || root==p || root==q) return root;
        TreeNode* leftAncestor = lowestCommonAncestor(root->left, p, q);
        TreeNode* rightAncestor = lowestCommonAncestor(root->right, p, q);
        if (leftAncestor && rightAncestor) return root;
        return leftAncestor?leftAncestor:rightAncestor;
    }
};