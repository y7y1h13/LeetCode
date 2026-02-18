from functools import lru_cache

class Solution:
    def climbStairs(self, n: int) -> int:
        
        @lru_cache(None)
        def dfs(x):
            if x <= 2:
                return x
            return dfs(x - 1) + dfs(x - 2)
        
        return dfs(n)
