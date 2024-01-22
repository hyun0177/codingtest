# 백준 1106 호텔 골5 30분 //
# sol
# 1. dp 배열의 값은 각 인덱스 명을 늘리는 데 필요한 최소 금액을 저장한다.
# 2. cost_info의 각 비용과 인원을 확인하면서 dp[i] = min(dp[i-people] + cost, dp[i]) 비교해 값을 저장한다.
# 3. +100 은 문제에서 얻을 수 있는 인원은 100보다 작은 자연수 라고 했기 떄문에, C 명 보다 최대 ~ +100 까지의 값이 더 저렴한 경우의 수가 있을 수 있기 떄문이다.
# 4. 따라서 마지막 출력 값도 dp[C] 의 값이 아닌 dp[C::] 의 값에서 최소값을 구하는 게 정답이 된다.

import sys

input = lambda : list(map(int, sys.stdin.readline().rstrip().split(' ')))

def solve(C, N, cost_info):
    dp = [0] + [ 1e6 for _ in range(C + 100) ]

    for cost, people in cost_info:
        for i in range(people, C + 101):
            dp[i] = min(dp[i-people] + cost, dp[i])

    print(min(dp[C::]))

def main():
    C, N = input()
    cost_info = [ input() for _ in range(N)]

    solve(C, N, cost_info)

if __name__ == "__main__":
    main()