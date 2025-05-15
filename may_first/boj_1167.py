import sys
sys.setrecursionlimit(10**6)    # 재귀 깊이 늘리기


V = int(input())

# 간선 정보 입력 배열
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    data = list(map(int, input().split()))
    # 기준 노드 
    node = data[0]
    idx = 1
    
    while data[idx] != -1:
        next_node = data[idx]
        weight = data[idx + 1]
        
        # (다음노드, 가중치)
        graph[node].append((next_node, weight))
        idx += 2

# DFS 함수
def dfs(node, dist):
    for next_node, weight in graph[node]:
		    
		    # 누적 거리 계산하기
        if visited[next_node] == 0:
            visited[next_node] = dist + weight
            # 다음 노드까지의 dist = dist + weight
            # 예) next_node = 2, 1->2 weight = 3 
            #      ---> 2까지의 거리는 5
            dfs(next_node, dist + weight)

# 아무 노드에서 가장 먼 노드 찾기
visited = [0] * (V + 1)
visited[1] = 1
dfs(1, 0)
# 가장 먼 노드 값 = visited 배열에서 가장 큰 값을 가지는 인덱스 
farthest_node = visited.index(max(visited))

# 가장 먼 노드에서 다시 가장 먼 노드 찾기
visited = [-1] * (V + 1)
visited[farthest_node] = 0
dfs(farthest_node, 0)

# 최대 거리 (지름)
print(max(visited))
