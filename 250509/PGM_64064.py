import re
from itertools import permutations

def is_match(banned, user):
    if len(banned) != len(user):
        return False
    for b, u in zip(banned, user):
        if b != '*' and b != u:
            return False
    return True

def solution(user_id, banned_id):
    result = set()

    for case in permutations(user_id, len(banned_id)):
        if all(is_match(b, u) for b, u in zip(banned_id, case)):
            result.add(frozenset(case))

    return len(result)
