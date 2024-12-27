/* 
Leetcode problem - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
*/

// Approach 1 - Take care of parent nodes by maintaing a map of TreeNode -> TreeNode 
// and stop till k th degree nodes are found

// The only reason we are maintaining visited array is because if you enqueue a node again (by lieu of it being 
// a root node of some other node apart from being the left/right node of current node, what will you do?)

class Solution {
private:
    unordered_map<TreeNode*, TreeNode*> parentMap; // Maps each node to its parent
    unordered_set<int> visited; // Keeps track of visited nodes

    // Populate parentMap with in-order traversal
    void inOrder(TreeNode* root) {
        if (!root) return;
        if (root->left) {
            parentMap[root->left] = root;
            inOrder(root->left);
        }
        if (root->right) {
            parentMap[root->right] = root;
            inOrder(root->right);
        }
    }

    // Perform BFS to find nodes at distance k
    vector<int> BFS(TreeNode* target, int k) {
        queue<TreeNode*> q;
        q.push(target);
        visited.insert(target->val);

        while (k > 0) {
            int size = q.size();
            while (size > 0) {
                TreeNode* top = q.front();
                q.pop();
                size--;

                // Add left child
                if (top->left && visited.find(top->left->val) == visited.end()) {
                    visited.insert(top->left->val);
                    q.push(top->left);
                }

                // Add right child
                if (top->right && visited.find(top->right->val) == visited.end()) {
                    visited.insert(top->right->val);
                    q.push(top->right);
                }

                // Add parent
                if (parentMap.find(top) != parentMap.end() &&
                    visited.find(parentMap[top]->val) == visited.end()) {
                    visited.insert(parentMap[top]->val);
                    q.push(parentMap[top]);
                }
            }
            k--;
        }

        // Collect the values of the nodes remaining in the queue
        vector<int> result;
        while (!q.empty()) {
            result.push_back(q.front()->val);
            q.pop();
        }
        return result;
    }

public:
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        // Populate parentMap
        inOrder(root);

        // Perform BFS to find nodes at distance k
        return BFS(target, k);
    }
};