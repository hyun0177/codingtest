#백준 10815 숫자 카드 실5 - 17분 소요

import sys

input = sys.stdin.readline

def solve(data, target):
    l = 0
    r = len(data) - 1

    while l <= r:
        mid = (l + r) // 2

        if data[mid] == target:
            return True
        elif data[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return

def main():
    N = int(input())
    sang = list(map(int, input().split()))

    M = int(input())
    deck = list(map(int, input().split()))

    sang.sort()

    for d in deck:
        print("1" if solve(sang, d) else "0", end=' ')

if __name__ == "__main__":
    main()