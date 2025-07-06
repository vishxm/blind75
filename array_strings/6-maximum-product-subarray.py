from typing import *

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        lb = ub = res = nums[0]

        for i, num in enumerate(nums):
            if i == 0:
                continue

            temp = max(num, ub*num, lb*num)
            lb = min(num, ub*num, lb*num)
            ub = temp
            res = max(res, ub)
        
        return res
