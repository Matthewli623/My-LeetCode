class Solution
{
public:
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2)
    {
        ListNode *real = new ListNode(0), *pre = real;
        while (l1 && l2)
        {
            if (l1->val > l2->val)
            {
                pre->next = l2;
                l2 = l2->next;
            }
            else
            {
                pre->next = l1;
                l1 = l1->next;
            }
            pre = pre->next;
        }
        pre->next = l1 ? l1 : l2;
        return real->next;
    }
};