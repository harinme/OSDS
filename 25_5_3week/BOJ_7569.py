# 리팩토링ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
from collections import deque

tomato_box = []

# 입력받기
M, N, H = map(int, input().split())

for h in range(H):
    # 한 판
    tomato_layer = []
    for n in range(N):
        tomato_oneline = list(map(int, input().split()))
        tomato_layer.append(tomato_oneline)
    # 토마토 박스
    tomato_box.append(tomato_layer)

result = 0
count = 0
day = deque()
next_day = deque()
if_all_matured = []

for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato_box[h][n][m] == 1:
                day.append((h, n, m))
            else:
                if_all_matured.append(0)

if len(if_all_matured) == 0:
    print(result)
    # 탈출
    exit()

# 이동
dm = [0, 0, -1, 1]
dn = [-1, 1, 0, 0]

# exit()문이 있으므로 else로 쓰지 않아도 됨
while day:
    h, n, m = day.popleft()

    # 앞뒤
    for nh in [-1, 1]:
        F_or_B = h + nh
        # if문 2개는 and로 써도 됨
        if 0 <= F_or_B < H and tomato_box[F_or_B][n][m] == 0:
            tomato_box[F_or_B][n][m] = 1
            next_day.append((F_or_B, n, m))

    # 상하좌우
    for i in range(4):
        nn = n + dn[i]
        nm = m + dm[i]
        if 0 <= nn < N and 0 <= nm < M:
            if tomato_box[h][nn][nm] == 0:
                tomato_box[h][nn][nm] = 1
                # visited[h][nn][nm] = 1
                next_day.append((h, nn, nm))

    # 마지막 날인 경우 제외: day는 비어있고 next_day는 존재할 때
    if not day and next_day:
        day = next_day
        next_day = deque()
        count += 1

# 결과값이 -1인지 확인: 0인 토마토가 남아 있는지 확인
# 들여쓰기 실수: while문 밖에서 확인
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato_box[h][n][m] == 0:
                print(-1)
                # 즉시 종료
                exit()

print(count)

# 제출용 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# from collections import deque

# M, N, H = map(int, input().split())
# tomato_box = []

# # 3차원 리스트
# for h in range(H):
#     tomato_box.append([])
#     for n in range(N):
#         tomato_oneline = list(map(int, input().split()))
#         tomato_box[h].append(tomato_oneline)

# result = 0
# count = 0

# # 얕은 복사
# # visited = [[[0] * M] * N] * H

# # ! 깊은 복사
# # visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
# day = deque()
# next_day = deque()
# if_all_matured = []

# h, n, m = 0, 0, 0

# # 토마토가 -1인 경우, 1인 경우, 0인 경우
# for h in range(H):
#     for n in range(N):
#         for m in range(M):
#             # temp = tomato_box[h][n][m]
#             # temp_v = visited[h][n][m]
#             # if tomato_box[h][n][m] == -1:
#             #     visited[h][n][m] = 1
#             if tomato_box[h][n][m] == 1:
#                 # visited[h][n][m] = 1
#                 day.append((h, n, m))
#             else:
#                 if_all_matured.append(0)

# # 위, 아래, 왼쪽, 오른쪽
# dm = [0, 0, -1, 1]
# dn = [-1, 1, 0, 0]

# # 0인 토마토가 없는 경우
# if len(if_all_matured) == 0:
#     print(result)
#     # ! 루프문이 아닌 경우
#     exit()

# else:
#     while day:
#         h, n, m = day.popleft()
#         # h, n, m = day.pop(0)

#         # 앞, 뒤
#         F, B = h - 1, h + 1
#         if h - 1 >= 0:
#             if tomato_box[F][n][m] == 0:
#                 tomato_box[F][n][m] = 1
#                 # visited[F][n][m] = 1
#                 next_day.append((F, n, m))

#         if h + 1 < H:
#             if tomato_box[B][n][m] == 0:
#                 tomato_box[B][n][m] = 1
#                 # visited[B][n][m] = 1
#                 next_day.append((B, n, m))

#         # 상하좌우
#         for i in range(4):
#             nn = n + dn[i]
#             nm = m + dm[i]
#             if 0 <= nn < N and 0 <= nm < M:
#                 if tomato_box[h][nn][nm] == 0:
#                     tomato_box[h][nn][nm] = 1
#                     # visited[h][nn][nm] = 1
#                     next_day.append((h, nn, nm))

#         # ! 마지막날이면 +1하지 않아도 됨
#         # ! 즉, 마지막날이 아닌지 확인하고 +1
#         if day == deque() and next_day:
#             day = next_day
#             next_day = deque()
#             count += 1

#     # 익지 않은 토마토가 있는 경우 -1 출력
#     # ! 3중 반복문 탈출
#     not_matured = False
#     for h in range(H):
#         for n in range(N):
#             for m in range(M):
#                 temp = tomato_box[h][n][m]
#                 if temp == 0:
#                     result = -1
#                     not_matured = True
#                     break
#             if not_matured:
#                 break
#         if not_matured:
#             break

#     # 결과가 -1이 아닌 경우
#     if result != -1:
#         result = count

# print(result)

# 테스트용 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# import sys
# sys.stdin = open('BOJ_7569.txt')

# from collections import deque

# tc = int(input())
# for _ in range(tc):
#     M, N, H = map(int, input().split())

#     tomato_box = []

#     # 3차원 리스트
#     for h in range(H):
#         tomato_box.append([])
#         for n in range(N):
#             tomato_oneline = list(map(int, input().split()))
#             tomato_box[h].append(tomato_oneline)

#     result = 0
#     count = 0

#     # 얕은 복사
#     # visited = [[[0] * M] * N] * H

#     # 깊은 복사
#     visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
#     day = deque()
#     next_day = deque()
#     if_all_matured = []

#     h, n, m = 0, 0, 0

#     # 토마토가 -1인 경우, 1인 경우, 0인 경우
#     for h in range(H):
#         for n in range(N):
#             for m in range(M):
#                 # temp = tomato_box[h][n][m]
#                 # temp_v = visited[h][n][m]
#                 if tomato_box[h][n][m] == -1:
#                     visited[h][n][m] = 1
#                 elif tomato_box[h][n][m] == 1:
#                     visited[h][n][m] = 1
#                     day.append((h, n, m))
#                 else:
#                     if_all_matured.append(0)
    
#     # 위, 아래, 왼쪽, 오른쪽
#     dm = [0, 0, -1, 1]
#     dn = [-1, 1, 0, 0]
    
#     # 0인 토마토가 없는 경우
#     if len(if_all_matured) == 0:
#         print(result)
#         continue

#     else:
#         while day:
#             h, n, m = day.popleft()
#             # h, n, m = day.pop(0)

#             # 앞, 뒤
#             F, B = h - 1, h + 1
#             if h - 1 >= 0:
#                 if tomato_box[F][n][m] == 0:
#                     tomato_box[F][n][m] = 1
#                     visited[F][n][m] = 1
#                     next_day.append((F, n, m))

#             if h + 1 < H:
#                 if tomato_box[B][n][m] == 0:
#                     tomato_box[B][n][m] = 1
#                     visited[B][n][m] = 1
#                     next_day.append((B, n, m))

#             # 상하좌우
#             for i in range(4):
#                 nn = n + dn[i]
#                 nm = m + dm[i]
#                 if 0 <= nn < N and 0 <= nm < M:
#                     if tomato_box[h][nn][nm] == 0:
#                         tomato_box[h][nn][nm] = 1
#                         visited[h][nn][nm] = 1
#                         next_day.append((h, nn, nm))

#             if day == deque():
#                 day = next_day
#                 next_day = deque()
#                 count += 1
            
#         if count > 0:
#             result = count - 1

#         # 익지 않은 토마토가 있는 경우 -1 출력
#         for h in range(H):
#             for n in range(N):
#                 for m in range(M):
#                     temp = tomato_box[h][n][m]
#                     if temp == 0:
#                         result = -1
#                         break

#     print(result)