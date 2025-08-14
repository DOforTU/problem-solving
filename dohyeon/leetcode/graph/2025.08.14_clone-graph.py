
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
           return None
       
        visited = {}
    
        def dfs(node):
               # 이미 복제된 노드라면 기존 복제본 반환
               if node in visited:
                   return visited[node]

               # 새로운 노드 생성 (값만 복사)
               clone = Node(node.val)
               visited[node] = clone

               # 이웃들을 재귀적으로 복제하여 연결
               for neighbor in node.neighbors:
                   clone.neighbors.append(dfs(neighbor))

               return clone

        return dfs(node)