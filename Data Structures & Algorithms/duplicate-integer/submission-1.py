class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        viewed = set()
        for x in nums:
            if x in viewed:
                return True
            viewed.add(x)
        return False

        