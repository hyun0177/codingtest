# 백준 10844 실1 31분 // case 3개로 나누어 생각
#case1: j==0 일때는 dp[i][j] = dp[i-1][1]
#case2: j==9 일때는 dp[i][j] = dp[i-1][8]
# case1, case2 즉 맨 앞 부분과 끝부분은 1->2 / 9-> 8 로 가는 가짓수가 1로 정해져 있다.
#case3: 1~8 일때는 ex 1->2 2->1 양방향으로 가능하기 때문에 dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
N = int(input())

dp = [[0 for _ in range(0)] for _ in range(N+1)]
for i in range(1, 10):
    dp[1][i] = 1

MOD = 1000000000

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N]) % MOD)