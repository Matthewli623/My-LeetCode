# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        no = 0
        cr = head

        d = ListNode(0, head)
        while cr:
            no += 1
            cr = cr.next

        tar = no - n
        no2 = 0
        pre = d

        while tar > 0:
            tar -= 1
            pre = pre.next

        pre.next = pre.next.next

        return d.next
