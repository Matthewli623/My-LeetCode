"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def __init__(self):
        self.visited={}
    
    
    def getclone(self,node):
        if not node:
            return None
        if node in self.visited:
            return self.visited[node]
        else:
            self.visited[node] = Node(node.val, None, None)
            return self.visited[node]
    
    
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        old = head
        newnode= Node(old.val,None,None)
        self.visited[old] = newnode
        
        
        while old != None:
            newnode.random=self.getclone(old.random)
            newnode.next=self.getclone(old.next)

            
            newnode=newnode.next
            old=old.next
            
        return self.visited[head]
            
            