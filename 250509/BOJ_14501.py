# 근무일수, 소요일, 수익
n = int(input())
t = []
p = []

# 입력받기
for _ in range(n):
    ti, pi = map(int, input().split())
    t.append(ti)
    p.append(pi)

# 완전탐색인가?

# 1 ~ N 일까지 얻을 수 있는 최대 수익
dp = [0] * (n + 1)

# 마지막 날부터 확인
# n=7이면 6, 5, 4, ..., 0
for i in range(n - 1, -1, -1):
    # 만약 인덱스(일자 - 1) + 소요일 <= N 이라면 (일자 초과 X)
    if i + t[i] <= n:
        # 상담 가능한 경우: 상담할때 vs 상담안할때 수익 비교
        dp[i] = max(p[i] + dp[i + t[i]], dp[i + 1])
        # 상담 불가한 경우: 전날은 다음날의 최댓값
    else:
        dp[i] = dp[i + 1]

# 최대 수익 출력
print(dp[0])