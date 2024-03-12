# 조합을 이용한 문제 풀이
# 시험볼떄는 import 자동완성 기능이 없다. 잘 기억해두자
# 몇개의 과목중에 몇명의 학생을 뽑아야할 것 같은 문제가 나오면 조합 사용을 고민해보자

from itertools import permutations

def solution(ability):
    ans = 0
    x = len(ability)
    y = len(ability[0])

    lst = list(permutations([i for i in range(x)], y))

    for l in lst:
        idx = 0
        tmp = 0
        for i in l:
            tmp += ability[i][idx]
            idx += 1
        if tmp > ans:
            ans = tmp

    return ans


PCCP모의고사 체육대회(조합).py
