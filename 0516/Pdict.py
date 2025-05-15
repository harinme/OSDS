"""
사전에 알파벳 모음 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는, 길이 5 이하의 모든 단어가 수록되 어 있습니다
사전에서 첫 번째 단어는 A이고, 그 다음은 AA이며, 마지막 단어는 UUUUU입니다

단어 하나 word가 매개변수로 주어질 때, 이 단어가 사전에서 몇 번째 단어인지 return하도록 solution 함수를 작성
"""

word = 'EIO'


letters = ['A', 'E', 'I', 'O', 'U']
dictionary = []

# 단어를 생성하며 진행
def dfs(curr):
    # 길이가 5를 넘어가면 stop
    if len(curr) > 5:
        return
    # 현재 단어를 딕셔너리에 저장
    if curr:
        dictionary.append(curr)
    # letters를 순회하며 현재 글자 + 다음 글자를 재귀
    for char in letters:
        dfs(curr + char)

dfs('')

# 인덱스는 0부터 시작하므로 + 1
print(dictionary.index(word) + 1)