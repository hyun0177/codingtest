#백준 2293 동전1 29분 // dp[i] += dp[i-c]

import sys

read_ints = lambda : list(map(int, sys.stdin.readline().rstrip().split(' ')))

def main():
    n, k = read_ints()
    coin = [ int(sys.stdin.readline().rstrip()) for i in range(n) ]

    dp = [ 0 for i in range(k+1) ]
    dp[0] = 1

    for c in coin:
        for i in range(c, k+1):
            if i - c >= 0:
                dp[i] += dp[i-c]
    print(dp[k])

if __name__ == "__main__":
    main()