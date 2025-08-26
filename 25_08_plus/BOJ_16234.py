import sys
from collections import deque
sys.stdin = open('input_16234.txt')

'''
왜 deque?
BFS에서 큐 연산(append, popleft)이 많아서, 
양쪽에서 O(1)로 넣고 빼는 deque가 리스트보다 효율적임
'''

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

di = [-1, 1, 0, 0]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
dj = [0, 0, -1, 1]

# 매일 BFS 탐색을 해...

def bfs(si, sj, unions):  # 시작 좌표니까 si, sj
    # 시작 좌표에서부터 BFS
    q = deque([(si, sj)])  # q.append((si, sj)) 와 동일
    unions[si][sj] = True
    states = [(si, sj)]
    state_sum = A[si][sj]

    # 큐가 빌 때까지 델타 탐색
    while q:
        # FIFO 방식으로 탐색 순서 유지
        i, j = q.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            # 범위 내, 연합에 포함되지 않은 경우(visited)
            if 0 <= ni < N and 0 <= nj < N and not unions[ni][nj]:
                # 인구 차이가 L 이상 R 이하
                if L <= abs(A[i][j] - A[ni][nj]) <= R:
                    unions[ni][nj] = True
                    q.append((ni, nj))
                    states.append((ni, nj))
                    state_sum += A[ni][nj]
    return states, state_sum

days = 0
while True:
    unions = [[False]*N for _ in range(N)]
    moved = False

    # 매일 BFS 탐색
    for i in range(N):
        for j in range(N):
            if unions[i][j]:
                continue
            states, state_sum = bfs(i, j, unions)
            
            # 연합이 생긴 경우에만 인구 이동
            if len(states) > 1:
                avg = state_sum // len(states)
                for x, y in states:  # 자동으로 튜플 언패킹
                    A[x][y] = avg
                moved = True

    # 인구 이동이 없으면 종료 (break)
    if not moved:
        break  # break 문은 가장 가까운 반복문 하나를 탈출
    
    # 인구 이동이 있든 없든 하루가 지남
    days += 1

print(days)