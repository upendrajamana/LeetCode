# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==0:
            return head
        current_left=head
        current_right=head
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1

        k = k % length
        if k == 0:
            return head
        for _ in range(k):
            current_right=current_right.next
        while current_right.next:
            current_left=current_left.next
            current_right=current_right.next
        new_head=current_left.next
        current_left.next=None
        current_right.next=head
        return new_head


