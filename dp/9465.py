#백준 9465 실1 24분 // 결국 최종 답은 max(dp[0][-1],dp[1][-1]) 가 최종 답이다.
# 이를 위해 열 별로 case를 따로 분리한다.
#1. DP[0][i] = max(DP[1][i - 2], DP[1][i - 1]) + arr[0][i]
#2. DP[1][i] = max(DP[0][i - 2], DP[0][i - 1]) + arr[1][i]
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    DP = [[0] * N for _ in range(2)]

    DP[0][0] = arr[0][0]
    DP[1][0] = arr[1][0]
    if N == 1:
        print(max(DP[0][0], DP[1][0]))
        continue

    DP[0][1] = arr[1][0] + arr[0][1]
    DP[1][1] = arr[0][0] + arr[1][1]
    if N == 2:
        print(max(DP[0][1], DP[1][1]))
        continue

    for i in range(2, N):
        DP[0][i] = max(DP[1][i - 2], DP[1][i - 1]) + arr[0][i]
        DP[1][i] = max(DP[0][i - 2], DP[0][i - 1]) + arr[1][i]

    print(max(DP[0][-1], DP[1][-1]))