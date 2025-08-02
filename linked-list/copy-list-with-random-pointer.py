"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr=head
        while curr:
            newNode=Node(curr.val)
            newNode.next=curr.next
            curr.next=newNode
            curr=newNode.next
        curr=head
        while curr:
            if curr.random:
                curr.next.random=curr.random.next
            curr=curr.next.next
        old_curr = head
        new_head = head.next
        new_curr = new_head

        while old_curr:
            old_curr.next = old_curr.next.next
            if new_curr.next:
                new_curr.next = new_curr.next.next
            old_curr = old_curr.next
            new_curr = new_curr.next

        return new_head
