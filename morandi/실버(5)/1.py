#백준 병약한 영정
from collections import defaultdict

import sys

input = sys.stdin.readline

def solve(d):
    R = int(input())

    for _ in range(R):
        lst = list(map(int, input().split()))
        lst.pop(0)
        res = []
        flag = True

        for l in lst:
            if not l in d.keys():
                flag = False
                break
            res.append(d[l])
        if flag:
            print(*res)
        else:
            print("YOU DIED")
def main():
    N = int(input())
    d = defaultdict(int)

    for _ in range(N):
        i, j = map(int, input().split())
        d[i] = j

    solve(d)

if __name__ == "__main__":
    main()
