# 14501 퇴사

# 특정 날짜에 상담을 할 건지 안 할 건지... 
# 1일차에 상담을 한다 -> 다음은 3일차로
# 1일차에 상담을 안 한다 -> 2일차로 
# 상담을 한다면 : 현재 날짜 n에서 n+T[n]일 후로 진행
# 상담을 하지 않는다면 : 다음 날 진행

def dfs(day, total):
    global ans
    # 1) 매 호출마다 지금까지 벌어들인 total로 ans 갱신
    ans = max(ans, total)

    # 2) 퇴사일까지 아직 남은 날이 있으면
    if day < N:
        # 2-1) 상담을 하지 않는 경우 : 다음 날로
        dfs(day + 1, total)
        # 2-2) 상담을 하는 경우 : 퇴사일 이전에 상담이 끝나면 day+T[day]일로 이동
        if day + T[day] <= N:
            dfs(day + T[day], total + P[day])

# 입력 처리
N = int(input())
T = []
P = []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

# 초기화 및 호출
ans = 0
dfs(0, 0)

# 결과 출력
print(ans)



