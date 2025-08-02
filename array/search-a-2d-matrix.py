class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def potential_row(matrix,target):
            low=0
            high=len(matrix)-1
            while low<=high:
                mid=(low+high)//2
                if matrix[mid][0]<=target<=matrix[mid][-1]:
                    return mid
                elif matrix[mid][0]<target:
                    low=mid+1
                else:
                    high=mid-1
            return -1
        def find(matrix,row):
            low=0
            high=len(matrix[0])-1
            while low<=high:
                mid=(low+high)//2
                if matrix[row][mid]==target:
                    return True
                elif matrix[row][mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return False
        row=potential_row(matrix,target)
        if row!=-1:
            result=find(matrix,row)
            return result
        else:
            return False