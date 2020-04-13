# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack= []
        stack2=[]
        times = 1
        adder=0
        pre =None
        while l1 or l2:
            if  l1:
                stack.append(l1.val)
                l1=l1.next
            if  l2:
                stack2.append(l2.val)
                l2=l2.next
        while stack or stack2:
            tempval=0
            if stack:
                tempval=stack.pop()
            if stack2:
                tempval+=stack2.pop()+adder
            if tempval>=10:
                if stack:
                    stack.append(stack.pop()+1)
                else :
                    stack.append(1)
            newNode=ListNode(tempval%10)
            newNode.next=pre
            pre=newNode
            
        return pre