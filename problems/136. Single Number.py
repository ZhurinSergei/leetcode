from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)): 
            res ^= nums[i]
            
        return res

a = Solution().singleNumber([1,2,3,4,5,5,4,2,1])