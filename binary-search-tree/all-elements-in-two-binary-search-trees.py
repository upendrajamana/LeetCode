# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,currlist):
            if not root:
                return
            self.inorder(root.left,currlist)
            currlist.append(root.val)
            self.inorder(root.right,currlist)
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        
        list1,list2,ans=deque(),deque(),[]
        self.inorder(root1,list1)
        self.inorder(root2,list2)
        while list1 and list2:
            ans.append(list1.popleft() if list1[0]<list2[0] else list2.popleft())
        return ans+list(list1)+list(list2)