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
    int carry = 0;
    
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if(l1 == NULL and l2 == NULL){
            if (carry == 0)
                return NULL;
            else
                return new ListNode(carry);
        }
        
        ListNode* head;
        if (l1 == NULL){
            head = new ListNode(carry + l2->val);
            l2 = l2->next;
        }
        else if (l2 == NULL){
            head = new ListNode(carry + l1->val);
            l1 = l1->next;
        }
        else{
            head = new ListNode(carry + l1->val + l2->val);
            l1 = l1->next;
            l2 = l2->next;
        }
        
        if (head->val > 9){
            carry = 1;
            head->val %= 10;
        }
        else
            carry = 0;
        
        head->next = addTwoNumbers(l1, l2);
        return head;
    }
};