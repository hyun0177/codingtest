# 백준 9084 dp 골5 20분 // 앞서 풀었던 동전 시리즈와 비슷한 방법으로 접근 ( 2293, 2294 ) 참고

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    dp = [ 0 for _ in range(m+1) ]
    dp[0] = 1

    for coin in coins:
        for i in range(m + 1):
            if i >= coin:
                dp[i] += dp[i - coin]

    print(dp[m])