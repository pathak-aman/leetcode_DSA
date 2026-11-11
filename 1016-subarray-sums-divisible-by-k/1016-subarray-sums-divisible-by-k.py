# 1. Generate all subarrays, compute the sums and check divisibilty add to count - O(n2)

# 2. Prefix
#              
# |------------||---------|
# [                      ,     ]
# |----------------------|
#  X = m*k + x
# mk = X - x
# mk % k = X%k - x%k
# X%k = x%k           
class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        n = len(nums)
        total = 0
        count = 0
        prefix_mod_count = {0:1}

        for i in range(n):
            total += nums[i]
            prefix_mod = total % k

            if prefix_mod in prefix_mod_count:
                count += prefix_mod_count[prefix_mod]
            
            prefix_mod_count[prefix_mod] = prefix_mod_count.get(prefix_mod, 0) + 1

        return count


# [4,5,0,-2,-3,1]; k = 5

# {
# 0: 1
# 1
# }

# i = 0
# total = 4
# prefix_mod = 4



