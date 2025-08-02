from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_frq=Counter(s)
        t_frq=Counter(t)
        for key in s_frq:
            if s_frq[key]!=t_frq[key]:
                return False
        return True
