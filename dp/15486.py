#백준 최사2 15486 dp 골5 // * 체감상 실버보다 쉬웠음

# sol
# 1. 예를 들어 dp[i]의 값이 3일, 30 이고 dp[i+1] 값이 3일, 25 라고 했을때 날짜는 동일하나 보수가 i가 더 높기 떄문에 그냥 단순히 해당 날과 이전 날의 크기를 비교하면 된다.
# 2. 하지만 여기서 고려해야될 부분이 소요기간이다. 해당 날짜 + 소요기간 - 1(당일) 이 퇴사까지 남은 기간인 N 의 값을 넘으면 안된다.
# 3. 따라서 final 이라는 변수에 스케쥴이 끝나는 당일의 날짜를 초기화 해주고 해당 날이 N 이하일때의 케이스를 만들어준다.
# 4. 여기서는 위에 단순히 크기를 비교한 값에다가 스케줄을 추가하는 개념이라고 생각하면 된다. 따라서 단순히 크기를 비교한 값과, 이전 날까지의 스케줄 + 새로운 스케쥴의 값 중 큰 값을 넣어준다.

import sys

input = sys.stdin.readline

def main():
    N = int(input())

    schedule = [ list(map(int, input().rstrip().split(' '))) for _ in range(N)]

    dp = [ 0 for _ in range(N+1)]

    for i in range(1, N+1):
        dp[i] = max(dp[i], dp[i-1])
        final = i + schedule[i-1][0] - 1
        if final <= N:
            dp[final] = max(dp[final], dp[i-1] + schedule[i-1][1])

    print(max(dp))

if __name__ == "__main__":
    main()