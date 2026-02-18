class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)
        
        def dfs(x):
            if x <= 2:
                return x
            if dp[x] != -1:
                return dp[x]
            dp[x] = dfs(x-1) + dfs(x-2)
            return dp[x]
        return dfs(n)