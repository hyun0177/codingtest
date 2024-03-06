import sys

read_int = lambda : list(map(int, sys.stdin.readline().rstrip().split(' ')))

def solve(N, bridge):
    dp = [ 1e6 for _ in range(N)]
    dp[0] = 0

    for i in range(1, N):
        for j in range(0, i):
            power = max((i - j) * (1 + abs(bridge[i] - bridge[j])), dp[j])
            dp[i] = min(dp[i], power)
    return dp[-1]
def main():
    N = read_int()[0]
    bridge = read_int()

    print(solve(N, bridge))

if __name__ == "__main__":
    main()