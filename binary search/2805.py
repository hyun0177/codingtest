# 백준 1805(실2) 나무자르기 // 19분
#다른 사람 풀이
# if t - mid > 0: 부분을 if t >= mid로 표현
#

import sys

read_ints = lambda: list(map(int, sys.stdin.readline().rstrip().split(' ')))

def sol(M, tree):
    l = 0
    r = max(tree)

    while l <= r:
        mid = (l + r) // 2

        res = 0
        for t in tree:
            if t - mid > 0:
                res += (t - mid)
        if res < M:
            r = mid - 1
        else:
            l = mid + 1

    print(r)

def main():
    N, M = read_ints()
    tree = read_ints()

    sol(M, tree)

if __name__ == "__main__":
    main()