import sys
sys.stdin = open("input_17144.txt", "r")

R, C, T = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(R)]
dust = []

# 공기청정기 위치
cleaner = []
for i in range(R):
    if map[i][0] == -1:
        cleaner.append(i)

def spread():
    # 모든 먼지 위치를 확인해
    for i in range(R):
        for j in range(C):
            if map[i][j] > 0:
                dust.append((i, j, map[i][j]))
    
    # 먼지가 확산이 되..
    for i, j, d in dust:
        spread_amount = d // 5
        # 4방향에 대해 탐색
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = i + dx, j + dy
            # 범위 내에 있고, 공기청정기가 아닐 때
            if 0 <= nx < R and 0 <= ny < C and map[nx][ny] != -1:
                # 한 방향씩 먼지 확산, 원래 위치에서 빼기
                map[nx][ny] += spread_amount
                map[i][j] -= spread_amount
                
    dust.clear()
    
def clean():
    cleaner_up = cleaner[0]
    cleaner_down = cleaner[1]
    
    # 위쪽 공기청정기, 반시계방향, 역순으로 칸 옮기기
    # 아래 화살표 방향
    for i in range(0, cleaner_up - 2):
        map[i + 1][0] = map[i][0]
    # 왼쪽 화살표 방향
    for j in range(1, C):
        map[0][j - 1] = map[0][j]
    # 위쪽 화살표 방향
    for i in range(1, cleaner_up):
        map[i - 1][C - 1] = map[i][C - 1]
    # 오른쪽 화살표 방향
    for j in range(1, C - 1):
        map[cleaner_up][j + 1] = map[cleaner_up][j]
    # 마지막으로 옮긴 칸은 0으로 채워주기
    map[cleaner_up][1] = 0
    
    # 아래쪽 공기청정기, 시계방향, 역순으로 칸 옮기기
    # 위 화살표 방향
    for i in range(cleaner_down + 2, R):
        map[i - 1][0] = map[i][0]
    # 왼쪽 화살표 방향
    for j in range(1, C):
        map[R - 1][j - 1] = map[R - 1][j]
    # 아래 화살표 방향
    for i in range(cleaner_down, R - 1):
        map[i + 1][C - 1] = map[i][C - 1]
    # 오른쪽 화살표 방향
    for j in range(1, C - 1):
        map[cleaner_down][j + 1] = map[cleaner_down][j]
    # 마지막으로 옮긴 칸은 0으로 채워주기
    map[cleaner_down][1] = 0
    
# T초동안 확산 후 정화
for _ in range(T):
    spread()
    clean()
    
# 남아있는 먼지 양 계산
result = 0
for i in range(R):
    for j in range(C):
        if map[i][j] > 0:
            result += map[i][j]
        
        # 그냥 마지막에 2 더하기
        # result += map[i][j]
# result += 2

