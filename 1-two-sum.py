from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_visit_dict = dict()
        for i, n in enumerate(nums):
            if target - n in num_visit_dict:
                return [num_visit_dict[target-n], i]
            num_visit_dict[n] = i

        return [-1, -1]
