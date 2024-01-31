#백준 2512 예산 실2 23분//

# 1. 이분탐색으로 상한액을 넘지않는 local값을 구한다음 구한 금액에서 1씩 증가시켜 상한액을 계산한다.
import sys
input = sys.stdin.readline

def solve(local, M):
    l = 0
    r = max(local)

    while l <= r:
        mid = (l + r) // 2
        total = 0
        for lo in local:
            if lo > mid:
                total += mid
            else:
                total += lo
        if total <= M:
            l = mid + 1
        else:
            r = mid - 1
    print(r)

def main():
    N = int(input())
    local = list(map(int, input().rstrip().split()))
    M = int(input())

    solve(local, M)

if __name__ == "__main__":
    main()