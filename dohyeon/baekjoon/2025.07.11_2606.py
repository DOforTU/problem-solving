# 문제
# 신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 
# 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

# 예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 
# 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 
# 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 
# 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.

# 어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 
# 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 컴퓨터의 수가 주어진다. 
# 컴퓨터의 수는 100 이하인 양의 정수이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 
# 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 
# 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

# 출력
# 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.

n = int(input())
m = int(input())
graph = {}
visited = set()

for _ in range(m):
    a, b = map(int, input().split())
    
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []

    graph[a].append(b)
    graph[b].append(a)

# dfs vs bfs 시간복잡도: 
# dfs: O(V + E) - V는 정점의 개수, E는 간선의 개수
# bfs: O(V + E) - V는 정점의 개수, E는
# 즉, 걸리는 시간은 같음

# 그래프 정렬 -> 이 문제에서는 굳이
# for key in graph:
#     graph[key].sort()

# 깊이 우선 탐색 (DFS)
def dfs(v, graph, visited):
    visited.add(v)

    for neighbor in graph.get(v, []):
        if neighbor not in visited:
            dfs(neighbor, graph, visited)

dfs(1, graph, visited)
print(len(visited) - 1)  # 1번 컴퓨터는 제외하고 출력