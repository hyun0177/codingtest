#백준 2624 동전 바꿔주기 골5 44분 //

import sys

read_ints = lambda : list(map(int, sys.stdin.readline().rstrip().split(' ')))

def solve(T, coin):
    dp = [ 0 for _ in range(T+1) ]
    dp[0] = 1

    for c, cnt in coin:
        for m in range(T, 0, -1):
            for i in range(1, cnt+1):
                if m - c * i >= 0:
                    dp[m] += dp[m-c*i]

    print(dp[T])

def main():
    T = int(input())
    k = int(input())
    coin = []

    for _ in range(k):
        coin.append(read_ints())

    solve(T, coin)

if __name__ == "__main__":
    main()