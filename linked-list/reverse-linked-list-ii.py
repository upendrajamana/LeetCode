# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        dummy=ListNode(0)
        dummy.next=head
        curr=head
        prev_node=dummy
        for i in range(left-1):
            prev_node=prev_node.next
            curr=curr.next
        sub=curr
        prev=None
        for i in range(right-left+1):
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        prev_node.next=prev
        sub.next=curr
        return dummy.next



