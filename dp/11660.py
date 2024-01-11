# 백준 11660 실1 42분 //
# 2. 누적 합을 구하는 점화식 과정
# [i][j] 까지의 합은 [i][j-1], [i-1][j] 각각의 합을 더한 후 중복되는 부분 즉 [i-1][j-1] + 구하고자 하는 칸의 크기 를 더하면 된다
# 위 설명대로 최종적인 점화식은 sum_dp[i][j] = sum_dp[i][j-1] + sum_dp[i-1][j] - sum_dp[i-1][j-1] + array[i-1][j-1]
# 1. 최종 답을 계산하는 과정
# sum_dp[x2][y2] 값에서 sum_dp[x1][y2] 와 겹치는 부분이 아닌 um_dp[x2][y1-1], sum_dp[x1-1][y2]을 뺴준다
# 위 과저에서 중복적으로 2번 빠지는 부분을 다시 더해주어야 한다. sum_dp[x1-1][y1-1]
# 따라서 최종적인 답을 구하는 식은 ans = sum_dp[x2][y2] - sum_dp[x2][y1-1] - sum_dp[x1-1][y2] + sum_dp[x1-1][y1-1]
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

array = []
for _ in range(n):
    array.append(list(map(int,input().split())))

sum_dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        sum_dp[i][j] = sum_dp[i][j-1] + sum_dp[i-1][j] - sum_dp[i-1][j-1] + array[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int,input().split())

    ans = sum_dp[x2][y2] - sum_dp[x2][y1-1] - sum_dp[x1-1][y2] + sum_dp[x1-1][y1-1]
    print(ans)