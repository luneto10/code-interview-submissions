class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # [3 3 2 3 2 1 3]
        # [2 3 3 3 2 1 3]
        # [2 2 3 3 3 1 3]
        # [2 2 1 3 3 3 3]
        
        for i, x in enumerate(nums):
            j = i + 1
            while j < len(nums) and nums[j] == val:
                j += 1
            if j >= len(nums):
                break
            nums[i], nums[j] = nums[j], nums[i]
        return len([x for x in nums if x != val])
            