from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        tmp_nums = set(nums)
        
        for i in range(len(nums) + 1):
            if i not in tmp_nums:
                return i