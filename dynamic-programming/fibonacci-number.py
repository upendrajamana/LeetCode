class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        list1=[0,1]
        for i in range(2,n+1):
            list1.append(list1[i-1]+list1[i-2])
        return list1[-1]