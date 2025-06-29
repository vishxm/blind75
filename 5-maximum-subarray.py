from typing import *

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = 0
        ans = 0
        for n in nums:
            temp += n
            temp = max(temp, 0)
            ans = max(ans, temp)
        return ans
