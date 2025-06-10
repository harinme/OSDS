'''
import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

card_num = int(input().rstrip())
card_list = []
for _ in range(card_num):
    card_list.append(int(input().rstrip()))

# print(card_list)
card_list.sort()
point = 1

card_sum = card_list[0]
while point < card_num:
    card_sum += card_list[point-1] + card_list[point]
    point+=1
print(card_sum)
'''

import sys
import heapq

# 로컬 테스트용 파일 열기 (제출 시에는 이 부분을 제거하세요)
sys.stdin = open('test.txt')
input = sys.stdin.readline

card_num = int(input().rstrip())
card_list = [int(input().rstrip()) for _ in range(card_num)]

# 카드 묶음이 하나뿐이라면 병합할 필요가 없으므로 0을 출력
if card_num <= 1:
    print(0)
    sys.exit()

# 최소 힙으로 만들어주기
heapq.heapify(card_list)

total_cost = 0
# 힙에 묶음이 2개 이상 남아있는 동안 반복
while len(card_list) > 1:
    # 가장 작은 두 묶음을 꺼내서 합친다
    a = heapq.heappop(card_list)
    b = heapq.heappop(card_list)
    merged = a + b
    
    # 비용에 더하고, 다시 힙에 넣는다
    total_cost += merged
    heapq.heappush(card_list, merged)

print(total_cost)
