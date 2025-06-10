import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

size, try_num = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(size)]
# print(matrix)
try_list = []
for _ in range(try_num):
    set = list(map(int, input().split()))
    try_list.append(set)

# print(try_list)

cnt = 0

while cnt < try_num:
    try_sum = 0
    x1, y1, x2, y2 = try_list[cnt]
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
    if x1 == x2:
        if y1 == y2:
            print(matrix[x1][y1])
        else:
            while y1 <= y2:
                try_sum += matrix[x1][y1]
                y1 += 1
            print(try_sum)
    else: ## x1 != x2
        for i in range(y1, size):
            try_sum += matrix[x1][i]
        x1+= 1
        # print(try_sum)
        while x1 <= x2:
            if x1 < x2:
                for i in range(size):
                    try_sum += matrix[x1][i]
            else:
                for i in range(0, y2+1):
                    try_sum += matrix[x1][i]
            x1+= 1
        print(try_sum)


    cnt += 1

# -----------------------

import sys
input = sys.stdin.readline

size, try_num = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(size)]

# 1) prefix 배열 생성 (1-based index)
prefix = [[0]*(size+1) for _ in range(size+1)]
for i in range(1, size+1):
    for j in range(1, size+1):
        prefix[i][j] = (
            matrix[i-1][j-1]
            + prefix[i-1][j]
            + prefix[i][j-1]
            - prefix[i-1][j-1]
        )

# 2) 쿼리 처리: O(1)
for _ in range(try_num):
    x1, y1, x2, y2 = map(int, input().split())
    # 1-based 로직에 맞춰
    res = (
        prefix[x2][y2]
        - prefix[x1-1][y2]
        - prefix[x2][y1-1]
        + prefix[x1-1][y1-1]
    )
    print(res)
