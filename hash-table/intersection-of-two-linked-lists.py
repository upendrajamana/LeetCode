# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def get_length(linked_list):
            length=0
            if not linked_list:
                return None
            else:
                while linked_list:
                    length+=1
                    linked_list=linked_list.next
            return length
        lenA,lenB=get_length(headA),get_length(headB)
        if not headA or not headB:
            return None
        while lenA>lenB:
            headA=headA.next
            lenA-=1
        while lenB>lenA:
            headB=headB.next
            lenB-=1
        while headA!=headB:
            headA=headA.next
            headB=headB.next

        return headA