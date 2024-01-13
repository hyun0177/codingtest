import sys
from collections import defaultdict

read_ints = lambda : list(map(int, sys.stdin.readline().rstrip().split(' ')))
def main():
    n = read_ints()[0]

    point_x = defaultdict(list)
    point_y = defaultdict(list)

    ans = 0

    for _ in range(n):
        i, j = read_ints()

        point_x[i].append(j)
        point_y[j].append(i)

    for k in point_x:
        if len(point_x[k]) >= 2:
            ans += 1
    for k in point_y:
        if len(point_y[k]) >= 2:
            ans += 1

    print(ans)

if __name__ == "__main__":
    main()