# 백준 9095 dp 실3 31120KB, 40ms
# 14분 // 경우의 수가 기존 식에서 +1, +2, +3 을 하는 경우의 수를 추가로 더해주면 되는 문제이므로, n-1, n-2, n-3 에서 각각 +1, +2, +3 을 더한 것이 dp[n]의 값들이 되므로 세 개를 더해주면 된다.

import sys

T = int(sys.stdin.readline())

dp = [ 0 for _ in range(12)]

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 12):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for _ in range(T):
    n = int(sys.stdin.readline())

    print(dp[n])