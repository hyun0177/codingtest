# 백준 2839 dp 실4 31120KB, 40ms
# n가지 기준으로 무엇을 나누어 갯수를 쌓아갈때 기준이 n, m 2가지면 i-n, i-m 을 기준( 전에 계산해뒀던 값) 으로 + 1 씩 계산하면서 문제에 따라 최소, 최대를 적절히 선택해 사용한다.

#sol1) 점화식 dp[i] = min(dp[i-3], dp[i-5]) + 1
import sys

N = int(sys.stdin.readline())

dp = [ 5001 for _ in range(5005)]

dp[3] = 1
dp[5] = 1

for i in range(6, N+1):
    dp[i] = min(dp[i-3], dp[i-5]) + 1

print(dp[N] if dp[N] < 5001 else -1)
