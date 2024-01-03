# 백준 2579 dp 실3 24분

import sys

read_int = lambda : list(map(int, sys.stdin.readline().rstrip().split(' ')))[0]

n = read_int()

s = [0]
dp = [0 for _ in range(n + 1)]

for _ in range(n):
    s.append(read_int())

if n < 3:
    print(sum(s))
else:
    dp[1] = s[1]
    dp[2] = s[1] + s[2]

    for i in range(3, n + 1):
        dp[i] = max((dp[i-3] + s[i-1] + s[i]), (dp[i-2] + s[i]))
        # case 1. +1 칸씩 올라가는 경우 연속 3번이 나오면 안되므로 -> dp[i-3]번째의 값이 +1.+1로 끝났을 경우가 있으므로 dp[i-3] + s[i-1] + s[i] 로 계산
        # case 2. +2 칸씩 올라가는 경우 -> dp[i-2] 번째 까지의 최대 값 + 현재 s[i] 값
    print(dp[n])
