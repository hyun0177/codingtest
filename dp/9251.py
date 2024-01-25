#백준 9251 골5 43분 // -> 2차원 배열 사용 생각하는 것이 오래걸렸음

#sol
# 1. dp의 2차원 배열을 dp[i][j]에서 각가 word1, word2 인덱스 값 i, j 라고 했을 때 i,j번쨰 글자까지의 최장 공통 부분의 문자열 길이를 저장한다.
# 2. case1. word1[i] == word2[j] -> 각 문자열에 i인덱스 값을 추가해주면 된다. 따라서 점화식은 dp[i][j] = dp[i-1][j-1] + 1
# 3. case2. word1[i] != word2[j] -> 이전의 dp값을 그대로 가져오면 공통된 길이를 가져올때 오류가 발생할 수 있다. word1, 2 의 마지막 글자가 다를 때에는
# 각 문자열의 마지막 글자들이 따로 한 글자씩 추가되었을 때의 max 값을 가져와야 한다. -> dp[i][j] = max(dp[i][j-1], dp[i-1][j])

import sys
input = sys.stdin.readline

word1 = input().strip()
word2 = input().strip()

h = len(word1)
w = len(word2)

dp = [ [ 0 for _ in range(w+1)] for _ in range(h+1) ]

for i in range(1, h+1):
    for j in range(1, w+1):
        if word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])