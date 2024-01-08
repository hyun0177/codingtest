# 백준 11055 실2 dp 22분 // for 문을 이용해 전의 수 보다 큰 경우에 대해서만 dp 값을 매기는데 이때 현재 dp[i] 값과 전 dp 값+ 현재 배열 값을 더한 값을 비교해 초기화한ㄷㅏ.
import sys

input = lambda : sys.stdin.readline()

def solve(n, arr):
    dp = [ 0 for _ in range(n)]

    dp[0] = arr[0]

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + arr[i])

    print(max(dp))

def main():
    n = int(input())
    arr = list(map(int, input().rstrip().split(' ')))

    solve(n, arr)

if __name__ == "__main__":
    main()