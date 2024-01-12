#백준 22869 실1 34분 //
# sol: 2중 for문을 이용해 경우의 수를 체크해 dp에 저장한다.
# dp에 들어갈 값은 dp[n] n에 도착할 수 있냐 없냐를 1, 0으로 나타낸다.
# 2중 for문을 이용해 i->j 까지 이동이 가능하며 dp[j]에 1을 넣어주고 최종적으로 dp[n-1]의 방문 여부를 확인해 정답을 출력한다.
import sys

read_ints = lambda : list(map(int, sys.stdin.readline().rstrip().split(' ')))

n, k = read_ints()
stone = read_ints()

dp = [ 0 for _ in range(n)]
dp[0] = 1

for i in range(n-1):
    for j in range(i+1, n):
        if dp[i] and (j - i) * (1 + abs(stone[j] - stone[i])) <= k:
            dp[j] = 1

print("YES" if dp[n-1] else "NO")
