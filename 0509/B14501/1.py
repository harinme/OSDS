
N = int(input())
# 걸리는 일 수 저장
T = []
# 이익 저장
P = []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

# dp 테이블
dp = [0] * (N + 2)

for i in range(N, 0, -1):
    # i + T[i - 1] 상담이 끝난 다음날
    # 상담을 할 수 있다면 = 상담이 끝나는 날이 퇴사일 전이라면
    if i + T[i - 1] <= N + 1:
        # 현재 상담의 이익 + 상담이 끝나는 날의 이익, 다음 날의 이익을 비교해서 더 큰 값을 저장
        dp[i] = max(P[i - 1] + dp[i + T[i - 1]], dp[i + 1])
    # 상담이 끝나는 날이 퇴사일 후면 이 상담은 못하니까 그 다음날과 같음
    else:
        dp[i] = dp[i + 1]


print(dp[1])