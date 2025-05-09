def matches(pattern, uid):
    """
    pattern: 불량 패턴 (예: "fr*d*")
    uid: 실제 사용자 아이디 (예: "frodo")
 
    """
    # 길이가 다르면 절대 매칭 불가
    if len(pattern) != len(uid):
        return False
    # 한 글자씩 비교
    for pc, uc in zip(pattern, uid):
        # 패턴 문자가 '*' 가 아니면서 실제 문자가 다르면 False
        if pc != '*' and pc != uc:
            return False
    return True

def solution(user_id, banned_id):
    # 1) 패턴별 후보군 뽑기
    cand = []
    for pat in banned_id:
        # matches로 필터링
        matched = [u for u in user_id if matches(pat, u)]
        cand.append(matched)

    results = set()

    # 2) 백트래킹: idx번째 패턴에 대해 used에 없는 후보만 골라 재귀
    def dfs(idx, used):
        if idx == len(banned_id):
            # 정렬해서 튜플로 만들어야 순서 상관없이 중복 제거 가능
            results.add(tuple(sorted(used)))
            return

        for u in cand[idx]:
            if u in used:
                continue
            dfs(idx + 1, used + [u])

    dfs(0, [])
    return len(results)
