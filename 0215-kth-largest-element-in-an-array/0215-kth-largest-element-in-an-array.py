import heapq as pq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Make a mix heap, push values
        # if exceeds k, the value at the root will never be a part of answer, so we pop
        min_heap = []
        for i in nums:
            pq.heappush(min_heap, i)

            if len(min_heap) > k:
                pq.heappop(min_heap)

        return min_heap[0]

