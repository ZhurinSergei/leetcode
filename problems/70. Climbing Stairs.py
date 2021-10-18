from typing import List

class Solution:
    storage = {0: 0, 1: 1, 2: 2}
    
    def climbStairs(self, n: int) -> int:
        
        return self._get_res(n)

    def _get_res(self, n):
        if n in self.storage:
            return self.storage[n]
        
        self.storage[n] = self._get_res(n - 1) + self._get_res(n - 2) 
        
        return self.storage[n]
    
 
for i in range(6):
    print(Solution().climbStairs(i))
        
