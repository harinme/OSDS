'''
백준 1463 1로 만들기

'''


from collections import deque

# 큐에 현재 숫자와 현재까지 계산한 카운트를 같이 넣음 
def solve():

    # [1] 입력받은 숫자가 1이면 0을 반환
    if k == 1:
        return 0
    
    # [2] 입력받은 숫자가 1이 아니라면 q에 초기값 k와 0을 삽입
    q = deque([(k, 0)])
    visited = [-1] * (k+1)  # 중복 계산 방지
    visited[k] = 1
    while q:
        cur_val, cnt = q.popleft()

        # [3] 먼저 cur_val을 각 분기별로 계산해준 뒤, 
        #     1이 있는지 확인하기 위해 리스트에 담아준다
        next_vals = []

        # (1) cur_val - 1
        next_vals.append(cur_val - 1)

        # (2) 2로 나누기
        if cur_val % 2 == 0:
            next_vals.append(cur_val // 2)

        # (3) 3으로 나누기
        if cur_val % 3 == 0:
            next_vals.append(cur_val // 3)

        # [4] next_vals 중에 1이 있는지 확인하고 있으면 cnt + 1 반환
        for next_val in next_vals:
            if next_val == 1:
                return cnt + 1
            
            # [5] 1이 없을 때, next_val이 1보다 크고 계산한 적이 없으면 
            if next_val > 1 and visited[next_val] == -1:
                visited[next_val] = 1           # 방문 처리
                q.append((next_val, cnt + 1))   # q 삽입, 다음 진행 

    return -1   # 1이 안 되면 -1 반환

k = int(input())
ans = solve()
print(ans)


# DP 풀이

# 거꾸로 이전 값에서 1 더하고, 2 곱하고, 3 곱하는 형태
# 예 ) 6의 경우, 5에서 1을 더하고, 3에서 2를 곱하고, 2에서 3을 곱함
# 여기서 계산 횟수가 가장 적은 값을 dp 테이블에 작성한다 

# 테이블 정의 dp = [0] * (N+1)
# 점화식 정의 dp[i] = min(dp[i-1]+1, dp[i//2]+1, dp[i//3]+1)


import sys
sys.stdin = open("1463_input.txt", "r")

N = int(input())

# DP 테이블 정의
dp = [0] * (N + 1)

# dp[1] = 0 초기값 설정

for i in range(2, N + 1):
    # 이전 값에서 +1 한 경우
    dp[i] = dp[i-1] + 1

    # dp[i] 가 2의 배수인 경우
    if dp[i] % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    
    # dp[i]가 3의 배수인 경우
    if dp[i] % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    
    
ans = dp[N]
print(ans)