# SWEA 나무 재테크 

# [1] 입력
N, M, K = map(int, input().split())  # N: 땅 크기, M: 나무 개수, K: 년 수
A_lst = [list(map(int, input().split())) for _ in range(N)]  # 겨울에 추가되는 양분 정보
arr = [[5] * N for _ in range(N)]  # 초기 양분은 모든 칸에 5

tree = [[[] for _ in range(N)] for _ in range(N)]   # 3차원
for _ in range(M):
    x, y, age = map(int, input().split())
    tree[x-1][y-1].append(age)
    

# K년동안 반복 
for _ in range(K):
    
    # 봄 + 여름
    for r in range(N):
        for c in range(N):
            
            # 나이순 처리를 위해 정렬
            tree[r][c].sort()
            
            for k in range(len(tree[r][c])):
                if tree[r][c][k] <= arr[r][c]:
                    arr[r][c] -= tree[r][c][k]
                    tree[r][c][k] += 1
                
                else:                           # 양분이 없는 경우
                    while k < len(tree[r][c]):  # 끝 나무부터 pop 
                        arr[r][c] += ( tree[r][c].pop() // 2 )
                    break   # 나가서 다음 칸으로..
    
    # 가을 : 나이가 5의 배수인 경우 인접 8칸에 나이 1짜리 나무 
    for r in range(N):
        for c in range(N):
            for k in range(len(tree[r][c])):    # 현 위치의 모든 나무 
                if tree[r][c][k] % 5 == 0:
                    for dr, dc in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                        nr, nc = r + dr, c + dc
                        if 0<=nr<N and 0<=nc<N:
                            tree[nr][nc].append(1)
                            
    # 겨울
    for r in range(N):
        for c in range(N):
            arr[r][c] += A_lst[r][c] 

                

ans = 0
for r in range(N):
    for c in range(N):
        ans += len(tree[r][c])

print(ans)



