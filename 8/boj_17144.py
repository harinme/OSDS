'''
백준 17144. 미세먼지 안녕!

1. 미세먼지가 있는 모든 칸에서 동시에 미세먼지 확산.
    - (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
    - 인접한 방향에 공기청정기가 있거나, 칸이 없으면 확산 안 됨.
    - 확산되는 양은 Ar,c/5이고 소수점은 버린다. -> 값이 5 이상이면 확산
    - (r, c)에 남은 미세먼지의 양은 Ar,c - ⌊Ar,c/5⌋×(확산된 방향의 개수) 이다.
    
2. 공기청정기가 작동한다.
    - 위쪽 공기청정기의 바람은 반시계방향으로 순환
    - 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
    - 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
    - 공기청정기로 들어간 미세먼지는 모두 정화된다.
'''
import sys
input = sys.stdin.readline

from copy import deepcopy

# [1] 청정기 위치 저장 position <- (i, j)
R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

position = []
for i in range(R):
    if arr[i][0] == -1:
        position.append(i)

up = position[0]
down = position[1]


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for _ in range(T):
    # [2] 확산 : 모든 위치 순회하면서 처리 arr[r][c] > 4 일 때만 처리
    # 동시에 확산 -> deepcopy를 해줌
    arr_tmp = deepcopy(arr)
    for r in range(R):
        for c in range(C):
            if arr[r][c] >= 5:
                t = arr[r][c] // 5 
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0<= nr < R and 0 <= nc < C and arr[nr][nc] != -1:
                        arr_tmp[r][c] -= t
                        arr_tmp[nr][nc] += t

    arr = arr_tmp   # 동시 확산 처리 
    
    # [3] 순환
    for i in range(up-1, 0, -1): # 0까지 포함시키면 arr[0][0] = arr[-1][0] 됨 
        arr[i][0] = arr[i-1][0]
    for j in range(0, C-1):
        arr[0][j] = arr[0][j+1]
    for i in range(0, up):
        arr[i][C-1] = arr[i+1][C-1]
    for j in range(C-1, 0, -1):
        arr[up][j] = arr[up][j-1]
        
    
    for i in range(down+1, R-1):
        arr[i][0] = arr[i+1][0]
    for j in range(0, C-1):
        arr[R-1][j] = arr[R-1][j+1]
    for i in range(R-1, down, -1):
        arr[i][C-1] = arr[i-1][C-1]
    for j in range(C-1, 1, -1):
        arr[down][j] = arr[down][j-1]
    
    arr[up][0] = arr[down][0] = -1
    # 공청기에서 나온 바람 
    arr[up][1] = 0
    arr[down][1] = 0

arr[up][0] = arr[down][0] = 0
ans = sum(map(sum,arr))
print(ans)
                    
# 5 이상인 미세먼지의 4방향이 범위내고 공기청정기가 없는 곳이라면 그 위치에 //5 추가 
# 동시에 일어나니까 arr_tmp 에 추가 -> 위에서 미리 arr 값을 복사 
# 끝나면 arr_tmp를 arr에 저장
# [3] 공기 순환
#       - 값을 시계, 반시계로 밀게 되면 안됨 
#       - 기준점을 잘 잡아야 됨 목적지 기준으로 ..
#       - 공기청정기 바로 위에 있는 값은 어차피 청정기 안에 들어가서 정화되니까
#       - 청정기 위 위의 값부터.. for (i1, 0, -1)  목적지가 청정기 위치인 (i1, i2) arr[i][0] <- arr[i-1][0]


# 위에서 아래로 내려오는 경우 i1-1이 목적지 -> i1 기준으로 움직임 -> for i in range(i1-1, 0, -1)  arr[i1][0] <- arr[i1-1][0]
# 복사하려면 맨 마지막에 복사되는 곳부터 거꾸로 진행해야 됨 
# 오른쪽에서 왼쪽으로 순환하는 경우, 0부터 c-1까지 거꾸로 복사를 해줘야 함
# 예시) 맨 처음 복사 : arr[1]의 값을 arr[0]에 복사