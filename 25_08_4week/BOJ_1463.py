import sys
sys.stdin = open('input_1463.txt', 'r')

t = int(input())

dp = [0] * (t + 1)
dp[1] = 0
    
for i in range(2, t + 1):
    # 기본적으로 1을 빼는 경우
    dp[i] = dp[i - 1] + 1
    
    # 2로 나누는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    
    # 3으로 나누는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[t])
