from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_list = [dict(Counter(s)) for s in strs]
        n = len(strs)
        result = []
        w_used = set()
        for i in range(n):
            if strs[i] in w_used:
                continue
            w_used.add(strs[i])
            temp = [strs[i]]
            for j in range(i + 1, n):
                if dict_list[i] == dict_list[j]:
                    temp.append(strs[j])
                    w_used.add(strs[j])
            result.append(temp)
            print(result)
        return result