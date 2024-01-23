#백준 2294 동전2 21분 // 'dp[i] = min(dp[i], dp[i-c] + 1)'

import sys

read_ints = lambda : list(map(int, sys.stdin.readline().rstrip().split(' ')))

def main():
    n, k = read_ints()
    coin = [ int(sys.stdin.readline().rstrip()) for i in range(n) ]

    dp = [ 10001 for i in range(k+1) ]
    dp[0] = 0

    for c in coin:
        for i in range(c, k+1):
            if dp[i] > 0:
                dp[i] = min(dp[i], dp[i-c] + 1)

    print(-1 if dp[k] == 10001 else dp[k])

if __name__ == "__main__":
    main()