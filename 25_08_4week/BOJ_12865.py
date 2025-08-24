import sys
sys.stdin = open('input_12865.txt', 'r')

# W의 합은 K 이하, V의 합이 최대가 되도록 해야 한다.
N, K = map(int, input().split())

weight = [0] * (N + 1)
value = [0] * (N + 1)

for i in range(1, N + 1):
    W, V = map(int, input().split())
    weight[i] = W
    value[i] = V

# 무게별 최대 가치 저장
dp = [0] * (K + 1)

# 물건 하나씩 넣어보기
for i in range(1, N + 1):
    # 현재 물건을 넣을 때의 최대 가치 구하기(예: 7kg 배낭에 6kg 물건이면 1kg일 때의 최대 가치 더하기)
    for j in range(K, weight[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

print(dp[K])