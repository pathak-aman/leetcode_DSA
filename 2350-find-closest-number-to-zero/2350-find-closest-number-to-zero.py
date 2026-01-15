# We want to kick out the larger element that doesn't belong to the closest number club
# -1,1
# Python max_heap:
# Kick out -> -1, so we store the (-distance, num)


import heapq as pq
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        max_heap = []
        for i in range(len(nums)):
            pq.heappush(max_heap, (-1 * abs(nums[i]), nums[i]))
        
            if len(max_heap) > 1:
                pq.heappop(max_heap)

        return max_heap[0][1]