# 백준 22857 실2 //
# 이중 for문을 이용해 현재 가르키는 값이 짝수라면 dp[i] += 1 을 해주고 홀수라면 cnt를 이용해 카운트 시켜 k가 되었을때 최종적 답인 dp[i] 값이 저장된다.
import sys

read_ints = lambda : list(map(int, sys.stdin.readline().rstrip().split(' ')))

n, k = read_ints()

arr = read_ints()

dp = [ 0 for _ in range(n + 1) ]

for i in range(1, n+1):
    cnt = 0
    for j in range(i, n+1):
        if arr[j-1] % 2 == 0: dp[i] += 1
        else:
            if cnt == k:
                break
            cnt += 1

print(max(dp))
