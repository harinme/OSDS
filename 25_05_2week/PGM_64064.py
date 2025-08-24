# 제재 아이디 목록의 경우의 수

# 순열 불러오기
from itertools import permutations

# 제재 아이디가 유저 아이디와 일치하는지 확인
def is_match(banned, user):
    # 길이가 다른 경우
    if len(banned) != len(user):
        return False
    # 제재 아이디와 유저 아이디의 튜플
    for b, u in zip(banned, user):
        # 제재 아이디가 문자이고 유저 아이디와 다를 경우
        if b != '*' and b != u:
            return False
    return True

def solution(user_id, banned_id):
    result = set()

    # 유저 아이디에서 제재 아이디 개수만큼 원소를 고른 모든 순열
    for case in permutations(user_id, len(banned_id)):
        # 모두 일치하는지 확인
        all_matched = True
        # 하나의 제재 아이디, 유저 아이디
        for i in range(len(banned_id)):
            banned = banned_id[i]
            user = case[i]
            # 일치하지 않는 경우
            if not is_match(banned, user):
                all_matched = False
                break
        # 일치하는 경우
        if all_matched:
            # 조합 안에 조합 넣기
            result.add(frozenset(case))

    return len(result)