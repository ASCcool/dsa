
// Problem link: https://leetcode.com/problems/reverse-nodes-in-k-group/

class Solution {
public:
    ListNode* reverseList(ListNode* head, int k) {
        ListNode *prev = nullptr, *next = nullptr, *curr = head;
        int count = 0;
        while (curr && count < k) {
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
            count++;
        }
        return prev; // New head of the reversed group
    }

    ListNode* reverseKGroup(ListNode* head, int k) {
        if (!head || k == 1) {
            return head; // Base case: no reversal needed
        }

        // Check if there are at least k nodes in the list
        ListNode* curr = head;
        int count = 0;
        while (curr && count < k) {
            curr = curr->next;
            count++;
        }

        if (count == k) {
            // Reverse the first k nodes
            ListNode* newHead = reverseList(head, k);

            // Recursively reverse the rest of the list
            // Reason we are doing this is because while reversing 
            // we are setting head's next pointer to nullptr
            // essentially after first gement it it like this ==> 2 -> 1(head) -> nullptr
            // so we have to use head->next to merge the current reversed segment to the next reversed segment
            head->next = reverseKGroup(curr, k);

            return newHead; // Return the new head of this group
        } else {
            // If fewer than k nodes remain, return the head as is
            return head;
        }
    }
};