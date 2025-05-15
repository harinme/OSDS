def solution(word):
    # 자리별 가중치
    weights = [781, 156, 31, 6, 1]
    # 모음 순서 매핑
    order   = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}

    answer = 0
    # 각 자리마다
    for i, ch in enumerate(word):
        answer += order[ch] * weights[i]  # 이전 모음 블록 수
        answer += 1                        # 자기 자신 한 칸

    return answer
