# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = 0
        
        result=ListNode(0)
        pre=result
        adder = 0
        while l1 or l2 or adder:
            temp = 0
            if l1:
                temp+=l1.val
                l1=l1.next
            if l2:
                temp+=l2.val
                l2=l2.next
            temp+=adder
            adder=0
            if temp>=10:
                adder=1
                temp=temp%10
            newNode=ListNode(temp)
            pre.next=newNode
            pre=newNode
        return result.next
            
            
            
            
            