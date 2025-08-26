import sys
sys.stdin = open('input_16235.txt')

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

def spring_summer():
    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                # 어린 나무부터 양분 흡수
                trees[i][j].sort()
                for k in range(len(trees[i][j])):
                    # 나무 나이보다 양분이 크거나 같은 경우
                    if nutrient[i][j] >= trees[i][j][k]:
                        nutrient[i][j] -= trees[i][j][k]
                        trees[i][j][k] += 1
                    # 나무 나이보다 양분이 작은 경우
                    else:
                        for _ in range(k, len(trees[i][j])):
                            # 여름이 되면 죽은 나무가 양분이 됨
                            nutrient[i][j] += trees[i][j][_] // 2
                        # 죽은 나무 제거
                        trees[i][j] = trees[i][j][:k]
                        break
                    
def autumn():
    for i in range(N):
        for j in range(N):
            # 나무가 있는 경우
            if len(trees[i][j]) >= 1:
                # 나무 나이가 5의 배수인 경우
                for k in range(len(trees[i][j])):
                    if trees[i][j][k] % 5 == 0:
                        # 8방향으로 나무 생성
                        for d in range(8):
                            ni = i + dr[d]
                            nj = j + dc[d]
                            # 범위 내일 때 나무 번식
                            if 0 <= ni < N and 0 <= nj < N:
                                trees[ni][nj].append(1)
                                
def winter():
    for i in range(N):
        for j in range(N):
            nutrient[i][j] += A[i][j]
            
def four_season():
    # K년이 지난 후
    for _ in range(K):
        spring_summer()
        autumn()
        winter()

N, M, K = map(int, input().split())

trees = [[[] for _ in range(N)] for _ in range(N)]
nutrient = [[5 for _ in range(N)] for _ in range(N)]

A = [list(map(int, input().split())) for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

# K년이 지난 후
four_season()

result = 0

for i in range(N):
    for j in range(N):
        if trees[i][j]:
            result += len(trees[i][j])
            
print(result)