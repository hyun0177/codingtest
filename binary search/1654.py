# 백준 1654 백준 실2 27분

import sys

read_ints = lambda : list(map(int, sys.stdin.readline().rstrip().split(' ')))
read_int = lambda : read_ints()[0]

def sol(N, lan):
    l = 1
    r = max(lan)

    while l <= r:
        count = 0
        mid = (l + r) // 2

        for la in lan:
            count += la // mid

        if count < N:
            r = mid - 1
        else:
            l = mid + 1

    print(r)

def main():
    K, N = read_ints()
    lan = []

    for _ in range(K):
        lan.append(read_int())

    sol(N, lan)

if __name__ == "__main__":
    main()