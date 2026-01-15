# We will maintain a heap of size k 
# Heap-club will include closest k elements to x
# We will kick out any element that is greater than our closest k elements
# We need to maintain a max-heap
# (mod_distance, number)

# Python:
# [1,3,5] k = 2, x = 3
# 1 is closer than 3, therefore to kick out 5, we need to store -5, so that in (-1,-1) & (-1,-5), (-1,-5) gets kicked out 
# (-distance, -number)

import heapq as pq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        max_heap = []
        for i in range(len(arr)):
            pq.heappush(max_heap, (-1 * abs(x-arr[i]), -1 * arr[i]))
        
            if len(max_heap) > k:
                pq.heappop(max_heap)

        final_elements = [-pq.heappop(max_heap)[1] for i in range(len(max_heap))]
        return sorted(final_elements)