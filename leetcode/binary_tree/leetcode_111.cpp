/* 
Leetcode problem - https://leetcode.com/problems/minimum-depth-of-binary-tree/ 
*/

// Approach 1 - ***** minDepth = 1 + min(L,R) *****

class Solution {
public:
    int minDepth(TreeNode* root) {
        if (root == NULL) return 0; // null
        if (root->left == NULL and root->right == NULL) return 1; // leaf node
        int l=INT_MAX, r=INT_MAX;
        if (root->left != NULL)
            l = minDepth(root->left);
        if (root->right != NULL)
            r = minDepth(root->right);
        // 1 + min(L,R)
        return 1 + min(l,r);   
    }
};

// Approach 2 - minDepth is encountered during BFS traversal whenever the first leaf node is found

class Solution {
public:
    int minDepth(TreeNode* root) {
        if (root == NULL) return 0;
        queue<TreeNode*> q;
        q.push(root);
        int depth = 1;
        while (!q.empty()) {
            int queueSize = q.size();
            while (queueSize>0){
                TreeNode* curr = q.front();
                q.pop();
                if (!curr->left && !curr->right) return depth;
                if (curr->left) {
                    q.push(curr->left);
                }  
                if (curr->right) {
                    q.push(curr->right);
                }
                --queueSize;             
            }
            depth += 1;
        }
        return 0;
    }
};