# 백준 11726 실3 24분
# // 타일링의 경우의 수는 2x1 로 끝나는 케이스와 1x2 2개로 끝나는 2가지 케이스가 있다. 따라서 1x2 2개로 끝나는 케이스 즉 n-2 의 값과 2x1 로 끝나는 케이스 n-1 번째의 dp값을 더해준다.
import sys

n = int(sys.stdin.readline())

dp = [ i for i in range(n + 1)]

if n >= 3:
    for i in range(3, n+1):
        dp[i] = (dp[i-2] + dp[i-1]) % 10007


print(dp[n] % 10007)# 점차 진행할수록 dp[i] 값이 너무 커져 오버플로우가 발생한다. 이를 방지하기 위해 10000을 넘는 최소 소수를 나누어 준다.