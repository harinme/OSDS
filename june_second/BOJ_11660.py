'''
구간합 구하기 5

문제
(x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성

풀이
0을 위, 왼에 패딩해주기 

'''

N, M = map(int, input().split())

arr = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

cnt_list = []
for _ in range(M):
    cnt_list.append(list(map(int, input().split())))

# 원본배열 말고 누적합 배열 만들기
prefix = [[0] * (N+1) for _ in range(N+1)]

# 누적합 배열 채우기
for i in range(1, N+1):
    for j in range(1, N+1):
        prefix[i][j] = arr[i][j] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

for x1, y1, x2, y2 in cnt_list:
    result = prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1]

    print(result)