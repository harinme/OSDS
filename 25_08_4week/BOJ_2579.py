import sys
sys.stdin = open('input_2579.txt', 'r')

t = int(input())

arr = [0] * (t + 1)
sum = [0] * (t + 1)

for i in range(1, t+1):
    n = int(input())
    arr[i] = n
    
sum[1] = arr[1]

# 계단이 2개 이상일 때
if t >= 2:
    sum[2] = arr[1] + arr[2]
    
# 계단이 3개 이상일 때
if t >= 3:
    for i in range(3, t+1):
        sum[i] = max(sum[i-2] + arr[i], sum[i-3] + arr[i-1] + arr[i])

print(sum[t])