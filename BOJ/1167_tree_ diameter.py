import sys
from collections import deque
# input = sys.stdin.readline
sys.stdin = open('test.txt')

V= int(input().rstrip())

def bfs(start):
    dist = [-1] * (V+1)
    que = deque([start])
    dist[start] = 0

    while que:
        node = que.popleft()

        for next, cost in adj_list[node]:
            if dist[next] == -1:
                dist[next] = dist[node] + cost
                que.append(next)
    max_dist = max(dist)
    max_node = dist.index(max_dist)
    return max_node, max_dist


adj_list = [[] for _ in range(V+1)]

for _ in range(V):
    data = list(map(int, input().split()))
    # print(data)

    for i in range(1, len(data)-1, 2):
        n1 = data[0]
        n2, cost = data[i], data[i+1]

        adj_list[n1].append((n2, cost))

## bfs를 두번해서 임의의 값이 아닌 실제 가장 먼 노드 한 쪽을 선택해서 bfs 탐색
max_node, max_dist = bfs(1)
result=bfs(max_node)
print(result[1])