# 백준 15724 실1 주짓수 ( 11660 과 비슷한 유형의 문제 )

# sol
# 1. 누적합으로 1,1 부터 n, m까지의 누적합을 모두 구해준다.
# 2. 입력받은 범위까지의 넓이를 구하기 위해서 누적합을 이용하는데 그 누적합의 범위는 1, 1 부터 i, j 까지라서 중복되는 부분을 삭제해야 한다.

import sys
input = sys.stdin.readline

n, m = list(map(int, input().split(' ')))
area = [list(map(int, input().split(' '))) for _ in range(n)]

dp = [ [0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = area[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for _ in range(int(input())):
    x, y, i, j = map(int, input().split(' '))
    print(dp[i][j] - dp[x-1][j] - dp[i][y-1] + dp[x-1][y-1])