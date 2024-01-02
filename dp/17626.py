#백준 17626 실3 => 110764 KB, 168ms

import sys
import math

n = int(sys.stdin.readline())

dp = [ i for i in range(n + 1)]

for i in range(2, n+1):
    for j in range(1, int(math.sqrt(i)) + 1):
        dp[i] = min(dp[i-j**2] + 1, dp[i])

print(dp[n])