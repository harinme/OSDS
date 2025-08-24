# 중복순열(곱집합)을 만듦
from itertools import product

def solution(word):
    # 모든 문자열을 담을 리스트
    words = []
    for i in range(1, 6):
        # repeat의 개수만큼 원소를 가지는 중복순열
        for case in product(['A', 'E', 'I', 'O', 'U'], repeat = i):
            # 튜플로 저장된 case를 튜플 -> 리스트 -> 문자열
            words.append(''.join(list(case)))
            
    # 문자열을 사전순으로 정렬!
    words.sort()
    # 인덱스는 1부터 시작하므로 + 1
    return words.index(word) + 1

# 테스트용ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# import sys
# sys.stdin = open('PGM_84512.txt')

# tc = int(input())
# for _ in range(tc):
#     input_word = input().strip('"')
#     result = solution(input_word)
#     print(result)