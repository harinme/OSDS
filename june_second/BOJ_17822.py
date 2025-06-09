'''
원판 돌리기

(i, 1)은 (i, 2), (i, M)과 인접하다.
(i, M)은 (i, M-1), (i, 1)과 인접하다.
(i, j)는 (i, j-1), (i, j+1)과 인접하다. (2 ≤ j ≤ M-1)
(1, j)는 (2, j)와 인접하다.
(N, j)는 (N-1, j)와 인접하다.
(i, j)는 (i-1, j), (i+1, j)와 인접하다. (2 ≤ i ≤ N-1)

d가 0이면 시계방향
d가 1이면 반시계 방향
번호가 x의 배수인 원판을 d방향으로 k칸 회전

원판에서 인접하면서 같은 수를 모두 지운다
인접하면서 같은 수가 없으면 평균을 구하고, 평균보다 큰 수는 +1, 작은 수는 -1

T번 회전시킨 후 원판에 적힌 수의 합 구하기

---------------------------------------------
[1] 시계/반시계로 회전하는 규칙

예시1)
2번 : 5 2 4 2 -> 2 5 2 4 (시계방향 1칸)
예시2)
3번 : 3 1 3 5 -> 1 3 5 3 -> 3 5 3 1 -> 5 3 1 3 (반시계 3칸)

시계방향이면 맨 뒤에 있는 숫자가 맨 앞으로 오고 
반시계 방향이면 맨 앞에 있는 숫자가 맨 뒤로 간다 
-----------------------------------------------
[2] 인접한 거 지우는 규칙 -> 배열이랑 똑같음 
각 숫자들을 행렬로 만들어서 상하좌우에 인접하고 같은 수가 있으면 지워준다 
지워주는 건 숫자 0으로 만들기 

숫자가 0이 아닌 것들 중에서 인접한 숫자 검사 
'''

N, M, T = map(int, input().split())

# x의 배수를 찾아야하니까 0 패딩 해주기 
circle = [[0] * (M+1)]  # 0번째 행 패딩
for _ in range(N):
    circle.append([0] + list(map(int, input().split())))

arr = [list(map(int, input().split())) for _ in range(T)]


# 숫자 이동시키는 함수 
def move(arr, x, d, k):

    for row_idx in range(1, N+1):
        # 행이 x의 배수면 마지막 숫자를 맨앞으로 보내기
        if row_idx % x == 0:
            nums = circle[row_idx][1:]  # x의 배수인 원형의 숫자들
            k_mod = k % M   # 회전 수 최적화

            # 시계 방향
            if d == 0:
                nums = nums[-k_mod:] + nums[:-k_mod]
            else: 
                nums = nums[k_mod:] + nums[:k_mod]
            circle[row_idx][1:] = nums  # 새롭게 할당


# 지워지는 숫자라면 일단 삭제 배열에 True 표시한 뒤, 
# 마지막에 한꺼번에 True인 것들만 0으로 만들어주기
def check(circle):
    # 삭제가 되지 않았으면 평균 계산 해야하니까 삭제 되었는지 확인할 배열 만들기 
    delete = [[False] * (M+1) for _ in range(N+1)]

    # 1번부터 N번까지 각 원판에 M개의 숫자
    for i in range(1, N+1):
        for j in range(1, M+1):
            num = circle[i][j]
            if num == 0:    # 만약 지워진 숫자라면 continue
                continue


            # 상,하 인접한 숫자들이 같은지 검사 
            for d in [-1, 1]:
                nd = i + d
                if 1 <= nd <= N and circle[nd][j] == num:
                    # 현재 숫자랑 상, 하에 있는 수가 같다면 삭제표시
                    delete[i][j] = delete[nd][j] = True

            # 좌,우 인접한 숫자들이 같은지 검사
            left = (j-1) if j > 1 else M
            right = (j+1) if j < M else 1

            # 왼쪽에 같은 수가 있으면 삭제배열에 True 표시
            if circle[i][left] == num:
                delete[i][j] = delete[i][left] = True
            # 오른쪽에 같은 수가 있으면 삭제배열에 True 표시
            if circle[i][right] == num:
                delete[i][j] = delete[i][right] = True

    # 한꺼번에 표시 
    # 삭제 배열에서 True가 나오면 해당 위치의 숫자를 0으로 만들고 deleted 표시
    deleted = False
    for i in range(1, N+1):
        for j in range(1, M+1):
            if delete[i][j]:
                circle[i][j] = 0
                deleted = True
    return deleted


def average(circle):
    total = 0   # 원판 전체 숫자
    cnt = 0     # 다 지워진 경우엔 cnt = 0

    for row in circle[1:]:  # 첫번째 행부터 검사
        for num in row:
            if num != 0:
                total += num
                cnt += 1
    if cnt == 0:
        return  # 다 지워지면 아무것도 안 함
    
    average = total/cnt

    for i in range(1, len(circle)):
        for j in range(len(circle[i])):
            if circle[i][j] == 0:
                continue 
            if circle[i][j] > average:  # 평균보다 큰 수는
                circle[i][j] -= 1   # -1 해주기
            elif circle[i][j] < average:
                circle[i][j] += 1


for x,d,k in arr:
    move(circle, x, d, k)
    if not check(circle):
        average(circle)
result = sum(sum(row) for row in circle[1:])
print(result)