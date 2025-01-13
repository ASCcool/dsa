// Problem statement: https://leetcode.com/problems/remove-linked-list-elements/description/ (EASY)

class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode *prev, *next, *temp;
        temp = head;
        while (temp) {
            next = temp->next;
            if (temp->val==val) {
                if (prev) {
                    // if your node for deletion is any node other than head node
                    prev->next=next;
                }
                else {
                    // move head forward by one node, if head itself is up for removal
                    head = head->next;
                }
                temp = next;
            }
            else {
                // normal traversal in case current node is not up for deletion
                prev = temp;
                temp = next;
            }
        }
        return head;
    }
};