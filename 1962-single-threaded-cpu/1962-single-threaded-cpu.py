import heapq as pq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        for i,task in enumerate(tasks):
            task.append(i)

        tasks.sort(key = lambda x: x[0])
        # print(tasks)

        i = 0
        time = tasks[0][0]
        min_heap = []

        processed_order = []

        while i < n or min_heap:
            while i < n and tasks[i][0] <= time:
                pq.heappush(min_heap, (tasks[i][1], tasks[i][2]))
                # print(time, min_heap)
                i += 1
            if min_heap:
                processing_time, idx = pq.heappop(min_heap)
                processed_order.append(idx)
                time += processing_time
            else:
                time = tasks[i][0]
        return processed_order

        
        return processed_order
        
            


        