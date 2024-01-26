# ???백준 2225 골5 합분해 1시간 13분 //
# sol
# 점화식을 세우기 위해 규칙을 찾는다
# 전체적으로 보면 n을 k-1개의 숫자로 나타내는 개수 n을 k-1개의 숫자로 나타내는 개수 * 0을 1개의 숫자로 나타내는 갯수 -> dp[k-1][n] * dp[1][0]
# n-1을 k개의 숫자로 나타내는 갯수 -> n-1을 k-1개의 숫자로 나타내는 갯수 + 0 을 1개의 숫자로 나타내는 갯수 +
# n-2을 k-1개의 숫자로 나타내는 갯수 + 1 을 1개의 숫자로 나타내는 갯수
# n-3을 k-1개의 숫자로 나타내는 갯수 + 2 을 1개의 숫자로 나타내는 갯수

# 최종적으로 도출되는 점화식은 dp[i][j] = (dp[i-1][j] + dp[i][j-1])

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[ 0 for _ in range(201)] for _ in range(201)]

for i in range(201): # K = 1 , K = 2 일떄는 111111, 23456 이므로 초기화
    dp[1][i] = 1
    dp[2][i] = i + 1

for i in range(2, 201):
    dp[i][1] = i
    for j in range(2, 201):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000

print(dp[k][n])