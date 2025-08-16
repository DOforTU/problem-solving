from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 그래프(인접 리스트) 생성
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)  # b -> a (b를 들어야 a를 들을 수 있음)
        
        # 방문 상태: 0=미방문, 1=방문중, 2=방문완료
        visited = [0] * numCourses

        def dfs(node: int) -> bool:
            if visited[node] == 1:  # 현재 탐색 경로에 다시 등장 → 사이클 발견
                return False
            if visited[node] == 2:  # 이미 방문 끝난 노드 → 문제 없음
                return True

            visited[node] = 1  # 현재 노드 방문 중
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            visited[node] = 2  # 탐색 끝남
            return True

        # 모든 노드에 대해 DFS 수행
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
