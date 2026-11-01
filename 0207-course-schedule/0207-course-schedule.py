from collections import defaultdict
from queue import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Course dependence (a,b) b -> a, b should be completed before a.
        # We can take this dependency as a directed edge representing prerequiiste.

        n = numCourses
        q = deque()

        def toposort(q, adj_list, indegrees):
            topo_order = []
            while q:
                curr = q.popleft()
                topo_order.append(curr)

                # Decrement the indegrees for the connections of curr
                for conn in adj_list[curr]:
                    indegrees[conn] -= 1
                    if indegrees[conn] == 0:
                        q.append(conn)
            
            return topo_order

        # Make the adj_list such that [a,b] edge is from b -> a
        adj_list = defaultdict(list)
        indegrees = [0 for i in range(n)] 
        for a,b in prerequisites:
            adj_list[b].append(a)
            indegrees[a] += 1
        

        # Insert all the nodes with indegree 0
        for i in range(n):
            if indegrees[i] == 0:
                q.append(i)
        
        result = toposort(q, adj_list, indegrees)
        
        
        return True if len(result) == n else False


        









