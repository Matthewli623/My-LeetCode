# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        dicta={}
        dictb={}
        
        a=headA
        b=headB
        
        while a or b:
            if a:
                dicta[a]=a
                
            if b:
                dictb[b]=b
                
            
            if a in dictb:
                return a
            if b in dicta:
                return b
            
            if a:
                a=a.next
            if b:
                b=b.next
            
        
        return None