#백준 1010 dp 다리놓기

# sol1) 수학 공식 사용 mCn    // 301120KB , 44ms

"""import sys

time = int(input());

for _ in range(time):
    N, M = list(map(int, sys.stdin.readline().rstrip().split(' ')))

    result1 = 1
    result2 = 1

    for i in range(M-N+1, M+1):
        result1 *= i

    for j in range(1, N+1):
        result2 *= j

    print(int(result1 // result2))"""


# sol2) dp 점화식 dp[n][m] = dp[n-1][m-1] + dp[n][m-1] 사용 // 301120KB , 40ms

import sys

case = int(sys.stdin.readline())

dp = [ [1 for i in range(31)] for j in range(31)]

for i in range(31):
    dp[1][i] = i

for i in range(2, 31):
    for j in range(i + 1, 31):
        dp[i][j] = dp[i-1][j-1] + dp[i][j-1];

for _ in range(case):
    N, M = list(map(int, sys.stdin.readline().rstrip().split(' ')))

    print(dp[N][M])

1