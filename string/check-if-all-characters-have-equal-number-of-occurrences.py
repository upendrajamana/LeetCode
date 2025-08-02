class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hash_map={}
        for i in s:
            if i not in hash_map:
                hash_map[i]=1
            else:
                hash_map[i]+=1
        all_vals=hash_map.values()
        return len(set(all_vals))==1