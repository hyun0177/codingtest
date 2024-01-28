#랩실에서 잘 자요
import sys
input = sys.stdin.readline

def solve(N, arr):
    d = []

    for i in range(1, N+1):
        if not i in arr:
            d.append(i)

    prev = 0
    result = 0
    for i in d:
        if prev:
            result += min(7, (i-prev)*2)
        else:
            result += 7
        prev = i

    print(result)

def main():
    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    arr = list(set(arr))
    arr.sort()

    solve(N, arr)

if __name__ == "__main__":
    main()