def matching(user_id, target):
    target_len = len(target)
    candidate_list = []
    for idx in range(len(user_id)):
        # 문자의 길이를 비교 후 같다면 이제 상세히 비교
        if len(user_id[idx]) == target_len:
            count = 0
            for j in range(target_len):
                if target[j] == '*' or target[j] == user_id[idx][j]:
                    count += 1
                else:
                    break
            # 문자가 일치하다고 판단되면 그 인덱스를 넣어준다.
            if count == target_len:
                candidate_list.append(idx)
    return candidate_list

def recur(cnt, start):
    global answer
    global path_list
    if cnt == targets_num:
        sorted_path = sorted(path)
        if sorted_path not in path_list:
            path_list.append(sorted_path)
            answer += 1
        return

    for i in range(start, targets_num):
        for j in candidate_user[i]:
            if used[j] == True:
                continue

            used[j] = True
            path.append(j)
            recur(cnt+1, i+1)

            used[j] = False
            path.pop()

    


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]

# 테스트 1
banned_id = ["fr*d*", "abc1**"]

# # 테스트 2
# banned_id = ["*rodo", "*rodo", "******"]
# # 테스트 3
# banned_id = ["fr*d*", "*rodo", "******", "******"]

# 총 찾아내야 하는 유저의 수
targets_num = len(banned_id)

# 각 ban id 별 가능한 후보 유저를 담을 리스트
candidate_user = [[] for _ in range(targets_num)]

for i in range(targets_num):
    candidate_user[i].extend(matching(user_id, banned_id[i]))

# print(candidate_user)

answer = 0
used = [False for _ in range(len(user_id))]
path= []
path_list = []

recur(0,0)

## programmers 제출 코드--------------------------------------------------------------

def solution(user_id, banned_id):
    def matching(user_id, target):
        target_len = len(target)
        candidate_list = []
        for idx in range(len(user_id)):
            # 문자의 길이를 비교 후 같다면 이제 상세히 비교
            if len(user_id[idx]) == target_len:
                count = 0
                for j in range(target_len):
                    if target[j] == '*' or target[j] == user_id[idx][j]:
                        count += 1
                    else:
                        break
                # 문자가 일치하다고 판단되면 그 인덱스를 넣어준다.
                if count == target_len:
                    candidate_list.append(idx)
        return candidate_list
    
    def recur(cnt, start):
        ## global(X) nonlocal(O)
        ## nonlocal : 종속 함수가 상위 함수의 변수를 사용하고 싶을 때
        nonlocal answer
        nonlocal path_list
        if cnt == targets_num:
            sorted_path = sorted(path)
            if sorted_path not in path_list:
                path_list.append(sorted_path)
                answer += 1
            return


        for i in range(start, targets_num):
            for j in candidate_user[i]:
                if used[j] == True:
                    continue

                used[j] = True
                path.append(j)
                recur(cnt+1, i+1)

                used[j] = False
                path.pop()

    
    targets_num = len(banned_id)

    # 각 ban id 별 가능한 후보 유저를 담을 리스트
    candidate_user = [[] for _ in range(targets_num)]

    for i in range(targets_num):
        candidate_user[i].extend(matching(user_id, banned_id[i]))

    # print(candidate_user)

    answer = 0
    used = [False for _ in range(len(user_id))]
    path= []
    path_list = []

    recur(0,0)
    return answer

print(solution(user_id, banned_id))