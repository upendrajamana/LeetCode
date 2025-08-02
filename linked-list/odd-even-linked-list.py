# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr=head
        new_curr=head.next
        start=new_curr
        while curr and new_curr and new_curr.next:
            curr.next=new_curr.next
            curr=curr.next
            new_curr.next=curr.next
            new_curr=new_curr.next
        curr.next = start
        return head