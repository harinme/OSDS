import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))

    # 누적합 계산
    prefix = [0] * (K + 1)
    for i in range(K):
        prefix[i + 1] = prefix[i] + files[i]

    # dp[i][j]: i~j까지 파일 합치는 최소 비용
    dp = [[0] * K for _ in range(K)]
    opt = [[0] * K for _ in range(K)]

    # 초기화
    for i in range(K - 1):
        dp[i][i + 1] = files[i] + files[i + 1]
        opt[i][i + 1] = i

    # 길이 3 이상 구간에 대해 DP 수행
    for length in range(2, K):
        for i in range(K - length):
            j = i + length
            dp[i][j] = float('inf')

            # 가능한 k 범위를 줄여주는 Knuth optimization
            for k in range(opt[i][j - 1], opt[i + 1][j] + 1):
                if k >= j:
                    continue
                cost = dp[i][k] + dp[k + 1][j] + prefix[j + 1] - prefix[i]
                if dp[i][j] > cost:
                    dp[i][j] = cost
                    opt[i][j] = k

    print(dp[0][K - 1])
