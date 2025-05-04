import sys
import heapq
sys.stdin = open('test.txt')
# 크루스칼, prim=> 모두를 이으면서 최소치를 찾으면 됨.

# prim으로 구현!

# 문자열을 숫자로 변환하기
# 아스키코드를 이용하여 대a소문자 구별 후 변환
def str_to_int(str):
    int = ord(str)

    if str.isupper(): # 문자열이 대문자라면
    # 아스키코드 A=65/ A =27 (- 38)
        int = int-38
    else: # 소문자라면
        # a = 97 / a = 1 (- 96)
        int = int - 96
    return int

# prim
def prim(start):
    que = []

    for next, cost in adj_list[start]:
        heapq.heappush(que, (cost, next))
    
    visited = [False] * V
    visited[start] = True
    total = 0
    used_edges = 0

    while que and used_edges < V-1:
        cost, c_node = heapq.heappop(que)

        if not visited[c_node]:
            visited[c_node] = True
            total += cost
            used_edges += 1

        for n_node, n_cost in adj_list[c_node]:
            if not visited[n_node]:
                heapq.heappush(que, (n_cost, n_node))

    return total


V = int(input())
matrix = [list(map(str, input().strip())) for _ in range(V)]


adj_list = [[ ] for _ in range(V)]

total_sum = 0
start_node = -1
for i in range(V):
    for j in range(V):
        if matrix[i][j] != '0':
            start_node = i
        break
    if start_node != -1:
        break

for i in range(V):
    for j in range(V):
        if matrix[i][j] == '0':
            matrix[i][j] = int(matrix[i][j])
        else:
            cost = str_to_int(matrix[i][j])
            if i !=j:
                matrix[i][j] = cost
                adj_list[i].append((j, cost))
                adj_list[j].append((i, cost))
            else: ## i == j
                matrix[i][j] = cost
        total_sum += matrix[i][j]

ok = True
for i in range(V):
    if not adj_list[0]:
        ok = False
    if not ok:
        break

if not ok:
    print(-1)
else:
    result = prim(start_node)
    total_sum -= result
    if total_sum < 0 :
        total_sum = -1
    print(total_sum)