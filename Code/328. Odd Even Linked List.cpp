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
    ListNode* oddEvenList(ListNode* head) {
        if(!head)return nullptr;
        ListNode* ev=head->next;
        ListNode* ans2=head->next;
        ListNode* od=head;
        while(od->next!=nullptr&&ev->next!=nullptr){
            od->next=od->next->next;
            ev->next=ev->next->next;
            od=od->next;
            ev=ev->next;
        }
        od->next=ans2;
        return head;
    }
};