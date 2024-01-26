# ***백준 5557 1학년 골5 41분 // 2차원 테이블 구성이 핵심
#sol
# 테이블 즉 dp 배열의 의미를 dp[i][j] -> i번째 숫자까지 계산하여 j를 만들 수 있는 경우의 수로 생각한다.
# 덧셈, 뺼셈의 경우의 수를 나누어 각 방법의 갯수를 더해 저장한다.
# 최종값은 dp에서 끝까지 계산한 결과 중 계산결과인 마지막 수를 만들 수 있는 방법의 갯수를 출력한다.

import sys
input = sys.stdin.readline

n = int(input())
dp = [ [0 for _ in range(21)] for _ in range(n)]
arr = list(map(int, input().split()))

dp[0][arr[0]] = 1

for i in range(1, n-1):
    for j in range(21):
        # 지난 계산했던 기록이 있는 행일 경우만 계산한다.
        if dp[i-1][j]:
            # 덧셈일 경우
            if 0 <= j+arr[i] <= 20:
                dp[i][j+arr[i]] += dp[i-1][j]
            # 뺄셈일 경우
            if 0 <= j-arr[i] <= 20:
                dp[i][j-arr[i]] += dp[i-1][j]

print(dp[n-2][arr[-1]])