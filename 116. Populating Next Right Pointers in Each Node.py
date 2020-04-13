"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import collections 
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:return root
        
        Q = collections.deque([root])
        
        while Q:
            qsize = len(Q)
            pre =None
            for i in range(qsize):
                node = Q.popleft()
                if node.right :Q.append(node.right)
                if node.left : Q.append(node.left)
                node.next=pre
                pre=node
        return root