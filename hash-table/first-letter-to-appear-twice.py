class Solution:
    def repeatedCharacter(self, s: str) -> str:
        unique=set()
        for i in s:
            if i in unique:
                return i
            else:
                unique.add(i)
        