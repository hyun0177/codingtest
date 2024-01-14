import sys

read_ints = lambda : list(map(int, sys.stdin.readline().rstrip().split(' ')))
read_int = lambda : read_ints()[0]

def solve(T):
    for t in range(T):
        n = read_int()
        arr = read_ints()
        res = []

        for a in arr:
            tmp = a * 4 / 3
            arr.pop(arr.index(int(tmp)))
            res.append(a)

        print(f"Case #{t+1}: ", end='')
        for r in res:
            print(r, end=' ')

def main():
    T = read_int()

    solve(T)

if __name__ == "__main__":
    main()