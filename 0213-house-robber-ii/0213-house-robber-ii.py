class Solution:
    def rob(self, nums: list[int]) -> int:
        # Recursion
        # nums = n houses.
        # f(ind) -> maximum loot from a circular array (0, ind) where adjacent elements are picked.
        # f(n-1) -> We want to find (0,n-1)

        # Circular array:
        # f(ind) and f(0) are now adjacent 
        # Therefore if f(ind) is selected we cannot chose f(0)

        def maxsum(ind, start, dp):
            # Base cases:
            if ind < start:
                return 0
            
            if dp[ind] != -1:
                return dp[ind]

            pick = nums[ind] + maxsum(ind-2,start,dp)
            notpick = 0 + maxsum(ind-1, start,dp)

            dp[ind] = max(pick, notpick)
            return dp[ind]
        
        n = len(nums)
        if n == 1:
            return nums[0]
        
        # Case I: Ignore the last house
        dp = [-1 for _ in range(n)]
        start = 0
        maxsum(n-2,start,dp)
        first = dp[n-2]
        # print(dp)

        # Case I: Ignore the first house
        dp = [-1 for _ in range(n)]
        maxsum(n-1,1,dp)
        last = dp[n-1]
        # print(dp)
        
        return max(first, last)

            


            



