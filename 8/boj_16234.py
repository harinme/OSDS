# 백준 16234 인구이동 

'''
순회하면서, 방문하지 않은 곳이면 bfs 처리
bfs 안에서 방문처리 이루어짐..

[1] flag = 0 / for r N, for c N / if not visited: bfs(r, c)
[2] for문을 다 돌고 연합이 1개 이상이면 flag = 1
[2] 그렇지 않으면 if flag == 0: break 
[2] 그렇지 않으면.. flag ==1 이면 ans += 1 

'''
from collections import deque

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0

# [1] 메인 루프 : 하루 단위로 시뮬레이션, visited 초기화, flag = 0 (오늘 연합여부)
while True:
    visited = [[0]*N for _ in range(N)]
    flag = 0
    q = deque()
    for r in range(N):
        for c in range(N):
            
            # [2] BFS : 방문하지 않은 곳이면 BFS 실행
            if not visited[r][c]:
                q.append((r, c))
                visited[r][c] = 1   # 방문 처리
                lst = [(r, c)]      # 연합을 구성하는 좌표 
                lst_sum = arr[r][c] # 연합 총 인구   나중에 sm // len(lst)
                
                
                while q:
                    sr, sc = q.popleft()
                    
                    for dr, dc in ((-1,0), (1, 0), (0, -1), (0,1)):
                        nr, nc = sr + dr, sc + dc 
                        if 0 <= nr < N and 0 <= nc <N and L <= abs(arr[sr][sc]-arr[nr][nc]) <= R:
                            if visited[nr][nc] == 0:
                                visited[nr][nc] = 1
                                lst.append((nr, nc))
                                lst_sum += arr[nr][nc]
                                q.append((nr, nc))  
                
                # [3] 연합 형성 : BFS 끝나고 연합 좌표 수가 2개 이상이면 연합 형성 
                if len(lst) > 1:
                    for i, j in lst:
                        arr[i][j] = lst_sum // len(lst)
                    flag = 1      # 연합 여부 
                    
    # [4] 종료 조건 : 하루가 끝났을 때 flag == 0 이면 break, 아니면 ans += 1
    if flag == 0:
        break
    ans += 1
    
print(ans)