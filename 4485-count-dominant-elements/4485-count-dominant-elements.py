class Solution:
    def countDominantElements(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        
        dom = 0
        if nums[0] >= nums[1]:
            dom += 1
        if nums[n-1] >= nums[n-2]:
            dom += 1

        for i in range(1,n-1):
            if nums[i] >= ((nums[i-1] + nums[i+1]) / 2):
                dom += 1
        
        return dom 