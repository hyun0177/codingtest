# 백준 1789 실5 이분 탐색 31분 // -> 처음 연습이라 생각보다 오래걸림

import sys
input = sys.stdin.readline

def main():
    S = int(input())

    ans = 0
    l = 1
    r = S

    while l <= r:
        mid = (l + r) // 2

        if mid * (mid + 1) // 2 <= S:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1

    print(ans)

if __name__ == "__main__":
    main()