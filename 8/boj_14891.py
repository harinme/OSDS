# 백준 톱니바퀴

''' 
초기 회전 톱니바퀴의 인덱스와 방향을 rotate_list에 입력 
해당 톱니바퀴의 오른쪽을 조사해서 조건에 맞으면 rotate_list에 추가 or break
동일하게 왼쪽 조사해서 rotate_list에 추가 or break

추가된 톱니바퀴 정보를 가지고 실제 회전 진행
deque의 rotate 사용 
'''
from collections import deque

arr = [deque(map(int, input().strip())) for _ in range(4)]
K = int(input())
# lst = [list(map(int, input().split())) for _ in range(K)]   # 회전 방법


for _ in range(K):
    
    idx, dr = map(int, input().split())
    idx -= 1
    # 맨 처음 인덱스와 방향을 rotate_list에 넣어줌
    rotate_list = [(idx, dr)]
    
    # 오른쪽 검사 
    d = dr
    for i in range(idx+1, 4):
        if arr[i-1][2] != arr[i][6]:
            d = -d
            rotate_list.append((i, d))
        else:
            break
    
    # 왼쪽 검사
    d = dr
    for i in range(idx-1, -1, -1):
        if arr[i][2] != arr[i+1][6]:
            d = -d
            rotate_list.append((i, d))
            continue
        else:
            break
        
    # 검사 끝내고 회전
    for idx, d in rotate_list:
        arr[idx].rotate(d)

ans = 0
for r in range(4):
    if arr[r][0] == 1:
        ans += 2**r
print(ans)