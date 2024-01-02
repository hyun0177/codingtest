# 백준 1463 실3 dp 26분 // 39368 KB , 552ms
import sys

n = int(sys.stdin.readline())

dp = [ 0 for _ in range(n+1)]

dp[1] = 0

for i in range(2, n + 1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[n])

# i%3 과 i%2 를 elif 로 작성하면 오류가 난다. 주의. // 또한 %3의 연산을 먼저해야 최소 계산 횟수가 계산되니 순서도 주의