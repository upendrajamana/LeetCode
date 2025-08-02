class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        hash1={}
        hash2={}
        for char in word1:
            if char not in hash1:
                hash1[char]=1
            else:
                hash1[char]+=1
        for char in word2:
            if char not in hash2:
                hash2[char]=1
            else:
                hash2[char]+=1
                
        for char in set(word1+word2):
            if abs(hash1.get(char,0)-hash2.get(char,0))>3:
                return False
        return True
            