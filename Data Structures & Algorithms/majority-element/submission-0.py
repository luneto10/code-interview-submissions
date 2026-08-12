class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Hashmap
        dict_counter = Counter(nums)
        max_value = 0
        max_key = None
        for k, v in dict_counter.items():
            if v > max_value:
                max_value = v
                max_key = k
        return max_key