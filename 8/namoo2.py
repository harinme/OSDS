'''
arr: 양분 정보
tree: (x, y, age) 튜플로 저장된 나무 정보
A_lst: 겨울에 추가되는 양분 정보
'''
from collections import deque
# [1] 입력
N, M, K = map(int, input().split())  # N: 땅 크기, M: 나무 개수, K: 년 수
A_lst = [list(map(int, input().split())) for _ in range(N)]  # 겨울에 추가되는 양분 정보
arr = [[5] * N for _ in range(N)]  # 초기 양분은 모든 칸에 5

tree = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, age = map(int, input().split())
    tree[x-1][y-1].append(age)
    
# 초기에 한번만 정렬
for r in range(N):
    for c in range(N):
        if tree[r][c]:
            tree[r][c] = deque(sorted(tree[r][c]))

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
# K년동안 반복 
for _ in range(K):
    
    for r in range(N):
        for c in range(N):
            # 해당 위치에 나무가 없으면 넘어가기
            if not tree[r][c]:
                continue
            # 기존 나무 리스트를 새롭게 갱신하기 위해
            # tree[r][c] 한 부분의 리스트를 나타내는 deque
            new_trees = deque()
            dead = 0
            
            cur_tree = tree[r][c]
            
            while cur_tree:
                age = cur_tree.popleft()
        
                if arr[r][c] >= age:
                    arr[r][c] -= age
                    new_trees.append(age + 1)
                else:
                    # 죽은 나무는 따로 저장
                    dead += age // 2
            tree[r][c] = new_trees
            arr[r][c] += dead

    # (수정하기) 번식한 나무들을 따로 저장해서 기존 tree 배열에 extend
    for r in range(N):
        for c in range(N):
            if not tree[r][c]:
                continue
            for age in tree[r][c]:
                if age % 5 == 0:
                    for dx, dy in directions:
                        nx, ny = r + dx, c + dy
                        if 0<=nx<N and 0<=ny<N:
                            tree[nx][ny].appendleft(1)

    for r in range(N):
        for c in range(N):
            arr[r][c] += A_lst[r][c]

ans = 0
for r in range(N):
    for c in range(N):
        ans += len(tree[r][c])

print(ans)