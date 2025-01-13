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

// Problem statement: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

// LCA for a Binary Search Tree (BST)

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (!root) return nullptr;
        // If both p and q are smaller than root, LCA lies in the left subtree
        if (p->val < root->val && q->val < root->val) {
            return lowestCommonAncestor(root->left, p, q);
        }
        // If both p and q are greater than root, LCA lies in the right subtree
        if (p->val > root->val && q->val > root->val) {
            return lowestCommonAncestor(root->right, p, q);
        }
        // If p and q are on opposite sides (or one of them is root), root is the LCA
        return root;
    }
};