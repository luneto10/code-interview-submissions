class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        cache = defaultdict(list)
        if n < 2:
            return False
        for i, val in enumerate(nums):
            cache[val].append(i)
        print(cache)
        
        for value, indexes in cache.items():
            idx_len = len(indexes)
            if idx_len < 2:
                continue
            print(value)
            for i in range(idx_len - 1):
                j = i + 1
                if abs(indexes[i] - indexes[j]) <= k:
                    return True
        return False
# 1 1 2 3
    # ^    