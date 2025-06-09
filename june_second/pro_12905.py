'''
가장 큰 정사각형 찾기 

문제
1와 0로 채워진 표,  표 1칸은 1 x 1 의 정사각형으로 이루어져 있음
표에서 1로 이루어진 가장 큰 정사각형을 찾아 넓이를 return 하는 solution 함수를 완성하기

풀이
누적합 처럼..? dp 배열을 만들고 dp[i][j]를 맨 오른쪽 아래 꼭짓점으로 가지는 정사각형
dp[i][j]는 그 정사각형 한 변의 길이로, 왼쪽 대각선 위로 뻗어갈 수 있는 정도를 보여준다

dp[i][j] = min(왼쪽, 위, 대각선) + 1
-> 가장 작은 길이를 최대 정사각형 길이로 정해야 사각형으로 확장될 수 있음

'''

def solution(arr):
    h = len(arr)
    w = len(arr[0])

    dp = [[0] * w for _ in range(h)]
    max_length = 0


    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:  # 기존 배열에서 1인 경우
                # [1] 정사각형이니까 i나 j중 0이 있으면 dp 무조건 1
                if i == 0 or j == 0:
                    dp[i][j] = 1

                # [2] 0이 아닌 경우, 왼쪽 위 대각선으로 뻗어나갈 수 있으면 정사각형 크기 늘어남
                # 이 때 최소 길이로 정해야 정사각형으로 확장할 수 있음 
                else:
                    dp[i][j] = min(
                        dp[i-1][j],     # 위
                        dp[i][j-1],     # 왼쪽
                        dp[i-1][j-1]    # 대각선
                    ) + 1 # 지금 내 위치까지의 길이 포함

                # 최대 정사각형 크기 갱신
                max_length = max(max_length, dp[i][j])
    return max_length **2   # 넓이

