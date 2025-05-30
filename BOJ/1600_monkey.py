import sys
from collections import deque

# 테스트용 입력 파일 열기
# input = sys.stdin.readline
sys.stdin = open('test.txt')

# 이동 방향 정의
dir = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 원숭이 이동 (상, 하, 좌, 우)
h_dir = [                                   # 말 이동 (8가지)
    (-2, -1), (-2, 1), (-1, -2), (-1, 2),
    (1, -2),  (1, 2),  (2, -1),  (2, 1)
]

def bfs(try_num, w, h, matrix):
    wall = 1
    road = 0

    # visited[k][y][x]: k번만큼 말 이동을 사용한 상태에서 (x,y) 방문 여부
    visited = [[[False] * w for _ in range(h)] for _ in range(try_num + 1)]
    q = deque()
    q.append((0, 0, 0, 0))  # x, y, used_horse_moves, distance
    visited[0][0][0] = True

    while q:
        x, y, used, dist = q.popleft()
        # 목표 지점 도착 시 최단 거리 반환
        if x == w - 1 and y == h - 1:
            return dist

        # 1) 원숭이 이동
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if (0 <= nx < w and 0 <= ny < h and
                matrix[ny][nx] == road and
                not visited[used][ny][nx]):
                visited[used][ny][nx] = True
                q.append((nx, ny, used, dist + 1))

        # 2) 말 이동 (아직 말 이동 기회가 남아 있을 때)
        if used < try_num:
            for dx, dy in h_dir:
                nx, ny = x + dx, y + dy
                if (0 <= nx < w and 0 <= ny < h and
                    matrix[ny][nx] == road and
                    not visited[used + 1][ny][nx]):
                    visited[used + 1][ny][nx] = True
                    q.append((nx, ny, used + 1, dist + 1))

    # 도달 불가능한 경우
    return -1

# 입력 처리
try_num = int(input().rstrip())
w, h = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(h)]

# 결과 출력
print(bfs(try_num, w, h, matrix))
