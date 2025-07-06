from typing import *

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        frontwards = [1] * n
        backwards = [1] * n
        res = [1] * n

        for i in range(1, n):
            frontwards[i] = frontwards[i-1]*nums[i-1]

        for i in range(n-2, -1, -1):
            backwards[i] = backwards[i+1]*nums[i+1]

        for i in range(n):
            res[i] = frontwards[i]*backwards[i]

        return res
