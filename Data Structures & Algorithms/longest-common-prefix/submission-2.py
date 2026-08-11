class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_prefix = float("inf")
        n = len(strs)
        for x in strs:
            n = len(x)
            if n < max_prefix:
                max_prefix = n
        
        longest = int(max_prefix)
        pointers = [0] * n
        for i in range(int(max_prefix)):
            lookup = set()
            for s in strs:
                lookup.add(s[i])
            if len(lookup) > 1:
                longest = i
                break
 
        return strs[0][:longest]
