class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup_dict = {}
        for i, num in enumerate(nums):
            remain = target - num
            lookup = lookup_dict.get(remain)
            if lookup is None:
                lookup_dict[num] = i
                continue
            return [min(i, lookup), max(i, lookup)]