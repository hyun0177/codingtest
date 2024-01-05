# 백준 11053 36분 // 문제 똑바로 이해하기.

import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().rstrip().split(' ')))

dp = [ 1 for _ in range(n)]

for i in range(1, n):
    for j in range(0, i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
# 중간에 다시 낮은 숫자부터 시작하는 가장 긴 부분수열이 있을 수 있기 때문에 모든 경우의 수를 따져봐야함
# 이중 for문을 이용해 i는 부분수열의 가장 맨 앞 기준점을 의미한다.
# j는 기준점 i 이전에 i보다 작은 값이 있는지 확인하고 있다면 dp[j]+1 을 아니라면 dp[i] 즉 1로 새로운 시작점을 의미한다.

print(dp)