
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x
        return True
    return False

N = int(input())
edges = []
total = 0

for i in range(N):
    row = input().strip()
    for j in range(N):
        c = row[j]
        if c == '0':
            continue
        # 문자 → 가중치
        if 'a' <= c <= 'z':
            weight = ord(c) - ord('a') + 27
        else:
            weight = ord(c) - ord('A') + 1
        total += weight
        if i != j:
            edges.append((weight, i, j))  # (가중치, 노드1, 노드2)

parent = [i for i in range(N)]
edges.sort()  # 가중치 오름차순 정렬

mst_cost = 0
edge_count = 0

for w, a, b in edges:
    if union(a, b):
        mst_cost += w
        edge_count += 1

# 모든 노드가 연결되었는지 확인
if edge_count == N - 1:
    print(total - mst_cost)
else:
    print(-1)
