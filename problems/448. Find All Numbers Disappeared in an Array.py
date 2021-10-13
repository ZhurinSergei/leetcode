from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        tmp_nums = set(nums)
        res = set()
        
        for i in range(1, len(nums) + 1):
            if i not in tmp_nums:
                res.add(i)
                
        return list(res)
