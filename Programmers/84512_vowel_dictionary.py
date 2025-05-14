'''
i -> 1563인데 i는 3번째 모음
1562가 사이클 두개
a = 781개 1 ~ 781
e = 781개 782~ 1562
i = 781개 1563 ~ 2343
u = 781개 2344 ~ 3124
사이클이 도는 거니까 시작하는 모음이 뭔지에 따라서 시작하는 수만 달라지면 됨
뒤에 오는 문자의 개수, 문자 배열은 a 사이클 한번만 돌리면 반복이라 그 값만큼 +해주기
'''
def solution(word):
    # 1) 모음 순서와, 사이클 시작 인덱스(각 글자마다 781개씩)
    vowel = ['A', 'E', 'I', 'O', 'U']
    start_num = {
        'A': 1,
        'E': 782,   # 1 + 781
        'I': 1563,  # 782 + 781
        'O': 2344,  # 1563 + 781
        'U': 3125   # 2344 + 781
    }

    # 2) 첫 글자 분리
    start = start_num[word[0]]
    words = word[1:]    # 뒤에 남은 글자들

    # 3) 단어 길이가 1이면 바로 반환
    if not words:
        return start

    # 4) 나머지 글자마다 남은 사이클 수를 더해준다
    answer = start
    # enumerate = 각 배열의 요소의 인덱스와 값을 튜플로 반환해줌
    for i, ch in enumerate(words):
        
        # 남은 단계: 4 - i
        # 한 글자 아래로 내려갈 때 돌게 되는 경우의 수 = 5^(남은 단계-1) + ... + 5^0
        cycle = sum(5**k for k in range(4 - i))
        answer += vowel.index(ch) * cycle

    # 5) 같은 글자 길이 그룹에서 자기 자신까지 포함
    answer += len(words)

    return answer


print(f"#1 {solution('AAAAE')}") # 6
print(f"#2 {solution('AAAE')}") # 10
print(f"#3 {solution('I')}") # 1563
print(f"#4 {solution('EIO')}") # 1189