#백준 14567 dp 골5 선수과목  24분 // -> 그래프 활용

# 그래프를 활용한다. 이어져있으면 그 전 dp값에서 +1 을해준다. 최종적으로 선수 과목의 수가 나온다,
#
import sys
read_ints = lambda : list(map(int, sys.stdin.readline().rstrip().split(' ')))

def solve(N, graph):
    dp = [ 1 for _ in range(N+1) ]

    for a, b in graph:
        if dp[b] <= dp[a]:
            dp[b] = dp[a] + 1

    print(*dp[1::])

def main():
    N, M = read_ints()

    graph = []

    for _ in range(M):
        i, j = read_ints()
        graph.append((i, j))
    graph.sort()

    solve(N, graph)

if __name__ == "__main__":
    main()