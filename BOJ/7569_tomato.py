import sys
from collections import deque
# from pprint import pprint
# sys.stdin = open('test.txt')
input = sys.stdin.readline

# 토마토가 다 익었는지 판단하는 함수
def is_ripe(matrix):
    result = True
    for box in matrix:
        for row in box:
            if 0 in row:
                result = False
                break
        if result == False:
            break
    return(result)

  

# 토마토 익히는 날짜를 계산하는 함수
def ripening(matrix):
    # 1인 곳(익은 토마토가 있는 곳을 찾는다)
    # 익은 토마토의 위치 값을 넣을 배열
    riped = deque()
    visited = list([
    [False for _ in range(cols)] for _ in range(rows)
] for _ in range(pages))

    # 전체 탐색하면서 인은 토마토 정보 추출
    for box in range(pages):
        for row in range(rows):
            for col in range(cols):
                if matrix[box][row][col] == 1:
                    
                    riped.append((box, row, col, 0))
                elif matrix[box][row][col] == -1:
                    visited[box][row][col] = True
    
    # 동시에 방문처리를 진행해야 하기 때문에 bfs로 접근
    max_cnt = 0
    
    up = -1
    down = 1
    stay = 0

    dir = [(up, 0, 0), # 박스 기준 위에 거
            (down, 0, 0), # 박스 기준 아래 거
            (stay, -1, 0), # 위로 이동
            (stay, 1, 0), # 아래로 이동
            (stay, 0, 1), # 오른쪽 이동
            (stay, 0, -1) # 왼쪽 이동
            ]

    while riped:
        c_box, c_row, c_col, c_cnt= riped.popleft()
        
        if c_cnt > max_cnt:
            max_cnt = c_cnt
        

        for i in dir:
            b_dir, r_dir, c_dir= i[0], i[1], i[2]
            nb, nr, nc = c_box + b_dir, c_row + r_dir, c_col + c_dir
            
            # 만약 범위 내에 있다면
            if 0 <= nb < pages and 0 <= nr < rows and 0 <= nc < cols:
                # 안 방문한 곳 = 빈 곳도 아니고, 아직 안 익은 곳도 아님
                if not visited[nb][nr][nc]:
                    visited[nb][nr][nc] = True
                    matrix[nb][nr][nc] = 1
                    riped.append((nb, nr, nc, c_cnt+1))

    if is_ripe(matrix):
        return max_cnt
    else:
        return -1


cols, rows, pages = map(int, input().split())
matrix_tomato = list([
    [] for _ in range(rows)
] for _ in range(pages))
# print(matrix_tomato) 

for box in range(pages-1, -1, -1):
    for row in range(rows):
        data = map(int, input().split())
        # print(data)
        matrix_tomato[box][row].extend(data)


# 만약 처음부터 토마토가 다 익어있었다면 더이상 수행할 필요 없음
if is_ripe(matrix_tomato):
    print(0)
else:
    # 안 익었다면 익히는 과정 수행해야 함.
    result = ripening(matrix_tomato)

    print(result)