class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1

        l = 0
        r = 1
        n = len(nums)

        while r < n:
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
            r += 1
        return l+1
