class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        pos_diagnal=set()
        neg_diagnal=set()
        res=[]
        board=[["."]*n for i in range(n) ]

        def backtrack(r):
            if r==n:
                copy=["".join(row)for row in board]
                res.append(copy)
                return 
            for c in range(n):
                if c in col or r+c in neg_diagnal or r-c in pos_diagnal:
                    continue
                col.add(c)
                pos_diagnal.add(r-c)
                neg_diagnal.add(r+c)
                board[r][c]="Q"
                backtrack(r+1)
                col.remove(c)
                pos_diagnal.remove(r-c)
                neg_diagnal.remove(r+c)
                board[r][c]="."
        backtrack(0)
        return res

            