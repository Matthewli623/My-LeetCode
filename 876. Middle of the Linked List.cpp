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
    ListNode *middleNode(ListNode *head)
    {
        ListNode *count = head, *out = head;
        int i = 1;
        while (count)
        {
            count = count->next;
            i++;
        }
        if (i % 2)
            i = i / 2;
        else
            i = i / 2 - 1;

        while (i > 0)
        {
            i--;
            out = out->next;
        }
        return out;
    }
};