"""
user_id와 banned_id가 매개변수로 주어질 때, 당첨에서 제외 되어야 할 제재 아디이 목록은 몇 가지 경우의 수가 가능한지 작성
"""
user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]

from itertools import permutations

# 각 banned_id에 맞는 user_id를 저장할 딕셔너리
my_dict = {}
for i in range(len(banned_id)):
    # banned_id의 값이 똑같을 수도 있으므로 인덱스와 함께 키로 저장(키는 중복된 값을 쓸 수 없음)
    my_dict[(i, banned_id[i])] = []
    banned = banned_id[i]

    for user in user_id:
        # 길이가 다르면 다음으로 넘어가기
        if len(banned) != len(user):
            continue
        else:
            # 각 id의 문자열을 하나하나 비교
            for j in range(len(banned)):
                # 별표라면 넘어가기
                if banned[j] == '*':
                    continue
                # 다른 부분이 있다면 break
                elif banned[j] != user[j]:
                    break
            # break 되지 않았다면 딕셔너리에 저장
            else:
                my_dict[(i, banned)].append(user)


# 중복없이 저장할 set
unique_set = set()

# user_id 중에서 banned_id 수만큼 순열 생성
for combo in permutations(user_id, len(banned_id)):
    # 생성된 순열 요소가 my_dict와 맞지 않다면
    for i, key in enumerate(my_dict):
        if combo[i] not in my_dict[key]:
            break
    # 모든 요소가 my_dict에 있다면 fronzenset로 추가(순서고려x)
    else:
        unique_set.add(frozenset(combo))

print(len(unique_set))

for i, key in enumerate(my_dict):
    print(i, key)