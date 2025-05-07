import sys
sys.stdin = open('test.txt')
# input = sys.stdin.readline

'''
N+1일 퇴사 최대한 많은 상담! 탐욕?
상담을 완료하는데 걸리는 기간, 금액
첫줄 =N
N줄의 걸리는 기간 및 금액
완전 탐색?
'''
def recur(cnt, r=False):
    global max_charge
    if (not r and cnt >= time_table[1][0] + 1) or (r and cnt >= days+1) :
        if cnt >= time_table[1][0]+1:     
            total = sum(path)
            if total > max_charge:
                max_charge = total
            return
    
    else:
        for i in range(cnt, days+1):
            c_day, c_charge = time_table[i][0], time_table[i][1]
            path.append(c_charge)

            recur(i+c_day, True)

            path.pop()
            


days = int(input().rstrip())
# 날짜가 자기 자신을 인덱스로 가지게 하려고
time_table = [[ ] for _ in range(days+1)]
for i in range(1, days+1):
    day, charge = map(int, input().split())
    if days + 1 - i < day:
        day, charge = 1, 0
    time_table[i].append(day)
    time_table[i].append(charge)
# print(time_table)
 
max_charge = 0
path = []

recur(1)
print(max_charge)