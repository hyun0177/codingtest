# 백준 2407 dp 실3 // 7분

import sys

n, m = list(map(int, sys.stdin.readline().rstrip().split(' ')))

dp = [ [1 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = int(dp[i][j-1] * (i - j + 1) // j)

print(dp[n][m])
