class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result=[]
        result.append([1])
        for  i in range(1,rowIndex+1):
            row=[]
            row.append(1)
            prev_row=result[-1]
            for  j in range(i-1):
                row.append((prev_row[j]+prev_row[j+1]))
            row.append(1)
            result.append(row)
        return result[rowIndex]