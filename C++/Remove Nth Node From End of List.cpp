/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* remove_pos = head;
        ListNode* pointer = head;
        
        // two pointers: one for finding the tail, the other for find the deleting node
        while(pointer != NULL){
            if(n >= 0)
                n--;
            else
                remove_pos = remove_pos->next;
            
            pointer = pointer->next;
        }
        
        if(n >= 0)
            head = head->next;
        else{
            remove_pos->next = remove_pos->next->next;
        }
        
        return head;
    }
};