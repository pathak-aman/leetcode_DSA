import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        result = []
        counter = {}
        for num in nums:
            counter[num] = counter.get(num,0) + 1

        for num, freq in counter.items():
            heapq.heappush(min_heap, (freq, num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        while min_heap:
            freq, num = heapq.heappop(min_heap)
            result.append(num)
        return result
