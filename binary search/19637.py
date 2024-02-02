#백준 19637 IF문 좀 대신 써줘 23분 //

import sys
input = sys.stdin.readline

def main():
    N, M = list(map(int, input().rstrip().split()))

    chingho = [ input().rstrip().split() for _ in range(N) ]
    chingho.sort(key=lambda x: int(x[1]))

    stat = [ int(input().strip()) for _ in range(M) ]

    for s in stat:
        r = len(chingho)
        l = 0
        res = 0
        while l <= r:
            mid = (l + r) // 2
            if int(chingho[mid][1]) >= s:
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        print(chingho[res][0])

if __name__ == "__main__":
    main()