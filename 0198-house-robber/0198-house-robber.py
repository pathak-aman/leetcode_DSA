class Solution:
    def rob(self, nums: list[int]) -> int:
        # Recursion
        # n houses.
        # f(n): The max sum of the sequence from (0,n), such that no adj element is picked
        # f(3): The max sum of the sequence from (0,3), such that no adj element is picked
        # We want f(n-1) -> sequences from nums[0] to nums[n-1] -> ?

        # def maxsum(ind):
        #     # Base cases:
        #     if ind == 0:
        #         # The only way to reach ind = 0, is previously picking ind = 2. Therefore we will pick this element.
        #         return nums[ind]
        #     if ind < 0:
        #         return 0

        #     pick = nums[ind] + maxsum(ind-2)
        #     notpick = 0 + maxsum(ind-1)

        #     return max(pick, notpick)



        def maxsum(ind, dp):
            # Base cases:
            if ind == 0:
                # The only way to reach ind = 0, is previously picking ind = 2. Therefore we will pick this element.
                return nums[ind]
            if ind < 0:
                return 0
            
            if dp[ind] != -1:
                return dp[ind]

            pick = nums[ind] + maxsum(ind-2, dp)
            notpick = 0 + maxsum(ind-1, dp)

            dp[ind] = max(pick, notpick)
            return dp[ind]

        n = len(nums)
        dp = [-1 for i in range(n)]

        return maxsum(n-1, dp)