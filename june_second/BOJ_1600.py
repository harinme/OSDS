'''
말이 되고픈 원숭이

입력
첫째 줄에 정수 K, 둘째 줄에 격자판의 가로길이 W, 세로길이 H
H줄에 걸쳐 W개의 숫자  0은 아무것도 없는 평지, 1은 장애물
시작점과 도착점은 항상 평지

풀이
- 최단거리 bfs
- 왼쪽위에서 오른쪽 아래로 이동하는데
- 현재 위치랑 말로 이동한 횟수 or 말로 이동할 수 있는 잔여 횟수 visited 배열
  visited[y][x][k] -> 현재 위치 (y,x)에서 말처럼 k번 이동
- 말의 이동 방향은 8방향 
- 맨 처음 bfs 큐 : deque([(0, 0, 0)]) 시작위치 맨 왼쪽 위, 말 이동 0번
- 매 단계마다 현재 위치(y,x)랑 말 이동 횟수 기록하기
- 다음 위치로 이동하면 말처럼 이동한 거랑 원숭이처럼 이동한 거 분리해서 시도 
- 이동하려는 곳이 0이고 아직 방문하지 않은 경우 큐에 추가 
- 맨 오른쪽 아래에 도착하면 return하고 못하면 -1 반환 

'''
from collections import deque

K = int(input())
W, H = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]

def horse_monkey(k, w, h, grid):
    # 말처럼 이동할 경우 방향
    horse = [(-2,-1), (-1,-2), (-2,1), (-1,2), (1,-2), (2,-1), (1,2), (2,1)]
    monkey = [(-1,0), (1,0), (0,-1), (0,1)]

    # 방문여부
    visited = [[[False] * (k+1) for _ in range(w)] for _ in range(h)]

    # 맨 처음 위치 방문처리
    visited[0][0][0] = True

    queue = deque()
    # 최단거리 계산해야하니까 이동횟수도 포함 
    queue.append((0, 0, 0, 0))  # 현재 위치, 말, 이동횟수

    while queue:
        y, x, horse_cnt, dist = queue.popleft()

        # 종료
        if y == h-1 and x == w-1:
            return dist
        
        # 원숭이처럼 이동
        for dy, dx in monkey:
            ny, nx = y+dy, x+dx
            
            if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] == 0 and not visited[ny][nx][horse_cnt]:
                visited[ny][nx][horse_cnt] = True
                queue.append((ny, nx, horse_cnt, dist + 1))

        # 말처럼 이동
        if horse_cnt < k:
            for dy, dx in horse:
                ny, nx = y + dy, x + dx
                if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] == 0 and not visited[ny][nx][horse_cnt+1]:
                    visited[ny][nx][horse_cnt+1] = True
                    queue.append((ny, nx, horse_cnt+1, dist+1))
    return -1 


print(horse_monkey(K, W, H, grid))
