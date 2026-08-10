class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = [sorted(x) for x in strs]
        dict_res = defaultdict(list)
        for i, x in enumerate(res):
            key = tuple(dict(Counter(x)).items())
            dict_res[key].append(strs[i])
        return list(dict_res.values())


