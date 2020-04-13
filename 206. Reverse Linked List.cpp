/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution
{
public:
    ListNode *reverseList(ListNode *head)
    {
        ListNode *pre, *cur;
        cur = head;
        pre = nullptr;
        while (cur)
        {
            ListNode *tep = cur->next;
            cur->next = pre;
            pre = cur;
            cur = tep;
        }
        return pre;
    }
};