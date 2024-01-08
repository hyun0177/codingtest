#백준 1912 dp 실2 35분 // dp 의 각 자릿수를 자릿수까지의 연속 합을 의미

import sys

input = lambda : sys.stdin.readline()

def solve(n, arr):
    dp = [ -1001 for _ in range(n)]

    dp[0] = arr[0]

    for i in range(1, n):
        if dp[i-1] > 0:
            dp[i] = dp[i-1] + arr[i]
        else:
            dp[i] = arr[i]

    return max(dp)

def main():
    n = int(input().rstrip())
    arr = list(map(int, input().rstrip().split(' ')))

    ans = solve(n, arr)

    print(ans)

if __name__ == "__main__":
    main()