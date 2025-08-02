# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKth(curr,k):
            while k>0 and curr:
                curr=curr.next
                k-=1
            return curr
        dummy=ListNode(0)

        groupPrev=dummy
        dummy.next = head
        while True:
            kth=getKth(groupPrev,k)
            if not kth:
                break
            groupNext=kth.next
            #reversing node
            prev,curr=kth.next,groupPrev.next
            while curr!=groupNext:
                next_node=curr.next
                curr.next=prev
                prev=curr
                curr=next_node
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        return dummy.next
    
        



        
            
        

