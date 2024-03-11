""
""" 내 풀이
def solution(s):

    s = s.lower().split(' ')
    ans = []

    for word in s:
        if word:
            ans.append(word[0].upper() + word[1:])
        else:
            ans.append(word)

    return ' '.join(ans)

print(solution("3people unFollowed me"))
"""

# 문자열s를 소문자로 바꾼 후 공백을 기준으로 나누줬다.
# 그 s에 대해 for문을 돌려 각각의 word에 대해서 word[0]만 대문자로 바꾸어준 후 ans에 append해서 마지막에는 list 상태인 ans를 join을 통해 문자열로 바꾸어 줬다,.

# 다른 사람의 풀이를 보니 간편한 함수가 있었다.
# capitalize() 함수는 문자의 첫 부분만 대문자로 바꾸어주는 내장 함수이다. 알아두면 유용할 것 같다.


"""다른 사람 풀이 법 capitalize() 함수 사용"""
def solution(s):

    s = s.lower().split(' ')
    ans = []

    for word in s:
        if word:
            ans.append(word.capitalize())
        else:
            ans.append(word)

    return ' '.join(ans)

print(solution("3people unFollowed me"))