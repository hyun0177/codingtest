#*** 백준 12865 골5 59분 // 2차원 배열로 생각하는 것이 좀 어려웠음

#sol
# 1. dp 배열의 설정을 2차원 배열로 한다. 여기서 d[n][k]가 의미하는 바는 n번째 물건까지 살펴보았을 떄, 무게가 k인 배낭의 최대 가치를 의미한다.
# 2. case1. 현재 배낭의 허용 무게보다 넣을 물건의 무게가 더 큰 경우 -> 넣지 않고 넘어간다.
# 3. case2. 1. 현재 넣을 물건의 무게만큼 배낭에서 뺀 후 현재 물건을 넣는다. // 2. 현재 물건을 넣지 않고 이전 배낭 그대로 가져간다.
# 4. 따라서 case별 점화식은 // 1. dp[i][j] = dp[i-1][j] // 2. dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v) 이다.
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
dp = [ [ 0 for _ in range(k+1)] for _ in range(n+1) ]

thing = [ list(map(int, input().split())) for _ in range(n) ]

for i in range(1, n+1): # 현재 담을 물건의 인덱스
    for j in range(1, k+1): # 허용 용량
        w = thing[i-1][0]
        v = thing[i-1][1]

        if j < w: # j
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[n][k])