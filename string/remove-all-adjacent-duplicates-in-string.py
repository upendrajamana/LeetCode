class Solution:
    def removeDuplicates(self, s: str) -> str:
        list1=[]
        for i in s:
            if list1 and list1[-1]==i:
                list1.pop()
            else:
                list1.append(i)
        return ''.join(list1)