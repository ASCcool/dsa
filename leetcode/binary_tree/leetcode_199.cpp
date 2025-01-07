// Problem link: https://leetcode.com/problems/binary-tree-right-side-view/description/
// For left side view, just do it at the very beginning, first element of any level's BFS

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> result;
        if (!root) return result;
        queue<TreeNode*> q;
        q.push(root);
        TreeNode *top=nullptr;
        int n;
        while (!q.empty()) {
            n = q.size();
            while (n>0) {
                top = q.front();
                q.pop();
                if (top->left) {
                    q.push(top->left);
                }
                if (top->right) {
                    q.push(top->right);
                }
                if (n==1) {
                    result.push_back(top->val);
                }
                n--;
            }
        }
        return result;
    }
};