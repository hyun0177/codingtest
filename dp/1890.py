#백준 1890 실1 21분 // 상, 하 두 case로 구분지어 그 전 위치 값을 더해 감 // bfs, dfs를 사용할 수 있지만 단순 구현으로 조금 더 편리하게 풀이될 수 있음

import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

direction = [(1, 0), (0, 1)]
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for x in range(N):
    for y in range(N):
        if x == y == N-1:
            print(dp[x][y])
            exit(0)

        dist = graph[x][y]
        if x + dist < N:
            dp[x + dist][y] += dp[x][y]
        if y + dist < N:
            dp[x][y + dist] += dp[x][y]