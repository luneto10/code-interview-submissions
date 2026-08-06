class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {k : i for i, k in enumerate(nums)}

        for i, num in enumerate(nums):
            remain = target - num
            element = index_map.get(remain)

            if element and element != i:
                return sorted([i, element])