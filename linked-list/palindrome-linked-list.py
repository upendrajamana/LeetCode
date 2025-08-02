# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if  not head or not head.next:
            return True
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        def reverse(node):
            prev=None
            curr=node
            while curr:
                next_node=curr.next
                curr.next=prev
                prev=curr
                curr=next_node
            return prev
        second_half=reverse(slow)
        first_half=head
        while second_half:
            if second_half.val!=first_half.val:
                return False
            second_half=second_half.next
            first_half=first_half.next
        return True
        

        
        