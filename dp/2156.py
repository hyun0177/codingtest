#백준 2156 실1 17분 // case 를 3개로 나누어 생각한다. //
#case1: 현재 와인은 마시는데 그 전 와인은 마시지 않는 경우 -> o o x o
#case2: 현재 와인은 마시는데 그 전와인도 마신 경우 -> o x o o
#case3: 현재 와인을 마시지 않는 경우 -> x o o x

import sys

input = lambda : sys.stdin.readline().rstrip()

def solve(n, arr):
    dp = [ 0 for _ in range(n) ]

    dp[0] = arr[0]

    if n > 1:
        dp[1] = dp[0] + arr[1]
    if n > 2:
        dp[2] = max(arr[2]+arr[1], arr[2]+arr[0], dp[1])
    for i in range(3, n):
        dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i], dp[i-1])

    return(dp[-1])

def main():
    n = int(input())
    arr = []

    for _ in range(n):
        arr.append(int(input()))

    print(solve(n, arr))

if __name__ == "__main__":
    main()