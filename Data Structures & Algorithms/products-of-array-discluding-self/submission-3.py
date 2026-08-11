class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        total_ex_zero = 1
        zeros_count = 0
        res = []
        for num in nums:
            total *= num
            if num == 0:
                zeros_count += 1
                continue
            total_ex_zero *= num 
        if zeros_count > 1:
                return [0] * len(nums)
        for num in nums:
            if zeros_count == 1:
                if num != 0:
                    res.append(0)
                else:
                    res.append(int(total_ex_zero))
            else:
                res.append(int(total / num))

        return res