# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result=ListNode(0)
        dummy=result
        carry=0
        while l1 or l2:
            total=0+carry
            if l1!=None:
                total+=l1.val
                l1=l1.next
            if l2!=None:
                total+=l2.val
                l2=l2.next
            carry=total//10
            total=total%10
            dummy.next=ListNode(total)
            dummy=dummy.next
        if carry==1:
            dummy.next=ListNode(1)
        return result.next
            
