# https://leetcode.com/problems/find-if-path-exists-in-graph/description/?envType=problem-list-v2&envId=graph

from collections import defaultdict
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        graph = self.create_graph(edges)
        return self.dfs(source, destination, visited, graph)
        
    def create_graph(self, edges: list[list[int]]):
        graph = defaultdict(list)
    
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
    
        return graph
    
    def dfs(self, node: int, destination: int, visited: set, graph: dict) -> bool:
        """It will be stop when it founds destination node"""
        if node == destination:
            return True

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                # dfs가 True를 반환하면 즉시 상위 호출에서도 True를 반환해야 함.
                if self.dfs(neighbor, destination, visited, graph):
                    return True

        return False