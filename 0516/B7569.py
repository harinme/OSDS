"""
보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토들의 영향을 받아 익게 된다
하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 방향에 있는 토마토를 의미한다.
대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 혼자 저절로 익는 경우는 없다고 가정한다.
철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자 모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지,
그 최소 일수를 구하는 프로그램을 작성하라
단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다
"""
from collections import deque

# 3차원 배열을 bfs 순회
# dfs로 해도 상관은 없을듯...?
def bfs(tomatos):
    # 탐색 경로 지정
    dz = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dx = [0, 0, 0, 0, 1, -1]

    # 큐
    queue = deque()

    # 토마토가 있으면 queue에 넣기
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if tomatos[z][y][x] == 1:
                    queue.append((z, y, x))
    # bfs 돌리기
    while queue:
        # 꺼내
        z, y, x = queue.popleft()
        # 경로 순회
        for i in range(6):
            nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
                # 범위에 있고 빈 칸이라면 다음 날짜를 저장
                if tomatos[nz][ny][nx] == 0:
                    tomatos[nz][ny][nx] = tomatos[z][y][x] + 1
                    # queue에 추가
                    queue.append((nz, ny, nx))

    result = 0
    for z in range(H):
        for y in range(N):
            for x in range(M):
                # 하다라도 빈 칸이 있다면 바로 -1 return
                if tomatos[z][y][x] == 0:
                    return -1
                # 최대값 갱신하며 진행
                result = max(result, tomatos[z][y][x])

    # 초기값이 0일 이므로 -1
    return result -1





M, N, H = map(int, input().split())

# 정수 1: 익은 토마토
# 정수 0: 익지 않은 토마토
# 정수 -1: 토마토가 들어있지 않은 칸

tomatos = []
for _ in range(H):
    tomatos.append([list(map(int, input().split())) for _ in range(N)])

print(bfs(tomatos))
