from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def amountOfTime(self, root: TreeNode | None, start: int) -> int:
        if root is None:
            return 0

        parent = {}
        burn_node = None

        def find_start_and_parents(node, parent_node):
            nonlocal burn_node

            if node is None:
                return

            if parent_node is not None:
                parent[node] = parent_node

            if node.val == start:
                burn_node = node

            find_start_and_parents(node.left, node)
            find_start_and_parents(node.right, node)

        find_start_and_parents(root, None)

        queue = deque([burn_node])
        visited = {burn_node}
        time = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                for neighbor in (node.left, node.right, parent.get(node)):
                    if neighbor is not None and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            if queue:
                time += 1

        return time