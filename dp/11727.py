# 백준 11727 실3 7분

import sys

n = int(sys.stdin.readline())

dp = [0 for _ in range(n + 2)]


dp[1] = 1
dp[2] = 3

if n > 2:
    for i in range(3, n + 1):
        dp[i] = (dp[i-1] + dp[i-2]*2) % 10007
        # 타일의 맨 끝에 끝나는 case는 총 3가지이다.
        # case 1. 타일의 끝이 1x2 로 끝나는 경우 -> 총 dp[n-1]가지
        # case 2. 타일의 끝이 2x1 두 개로 끝나는 경우 -> 총 dp[n-2]가지
        # case 3. 타일의 끝이 2x2 로 끝나는 경우 -> 총 dp[n-2]가지
        # 따라서 케이스 별로 종합한 최종 점화식은 dp[i] = (dp[i-1] + dp[i-2]*2)
print(dp[n] % 10007)