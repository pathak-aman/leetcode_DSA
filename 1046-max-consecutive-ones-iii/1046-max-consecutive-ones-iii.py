class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:

        # Brute -
        # 1. Generate all possible subarrays.
        # 2. Count ones + k 0s, 3. Return max

        # Two Pointers
        # zeros = 0


        l = 0
        r = 0
        n = len(nums)
        zeros = 0
        max_length = 0 

        while r < n:
            # Expansion
            if nums[r] == 0:
                zeros += 1
            
            # Invalidity - Shrink
            if zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            
            # Validity - Store:
            if zeros <= k:
                max_length = max(max_length, r - l + 1)
    
            r += 1
        return max_length
