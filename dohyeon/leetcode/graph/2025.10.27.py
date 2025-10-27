"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that 
you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. 
If there are many valid answers, return any of them. 
If it is impossible to finish all courses, return an empty array.

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. 
Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
"""

from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """dfs를 통해서 각 노드별로 방문을 안 했을 경우 0, 방문 중일 경우 1, 방문 완료일 경우 2로 표시.
        - '방문 중'의 의미는 현재 dfs 탐색 경로에 있다는 의미이며, 수강 순서를 담는 result 배열에 추가되기 전 상태를 의미.
            - 발견 했는데, 왜 result에 추가를 안하는 이유는 선수 과목이 있기 때문에 
                모든 선수 과목이 다 방문 완료가 되어야만 수강 순서에 추가할 수 있기 때문.
        - '방문 완료'의 의미는 해당 노드의 모든 인접 노드(선수 과목)를 다 방문하여 수강 순서에 추가된 상태를 의미.
        - '방문 중'일 때 다시 방문하게 된다면 사이클이 발생한 것이므로 빈 배열을 반환"""
        if numCourses == 0:
            return [0]
        
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a) # b -> a (b를 들어야 a를 들을 수 있음)
        
        visited = [0] * numCourses
        result = []

        def dfs(course):
            if visited[course] == 1:  # 현재 탐색 경로에 다시 등장 -> 사이클 발견
                return False
            if visited[course] == 2:
                return True

            visited[course] = 1  # 현재 노드 방문 중

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            
            visited[course] = 2  # 탐색 끝남
            result.append(course)  # 모든 선수 과목 방문 완료 후 수강 순서에

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return result[::-1]  # 후위 순회이므로 뒤집어서 반환
    
# Example usage:
solution = Solution()
print(solution.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))  # Output: [0,2,1,3] or [0,1,2,3]