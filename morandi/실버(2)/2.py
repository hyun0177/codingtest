import sys
from collections import defaultdict

read_str = lambda : list(map(str, sys.stdin.readline().rstrip().split(' ')))

def solve(menu_A, menu_B, menu_C):
    A_price = 0
    B_price = 0
    B_cnt = 0
    C_cnt = 0

    for _ in range(int(input())):
        order = sys.stdin.readline().rstrip()

        if order in menu_A.keys():
            A_price += menu_A[order]
        elif order in menu_B.keys():
            B_price += menu_B[order]
            B_cnt += 1
        else:
            C_cnt += 1

    res = "Okay"
    if A_price < 20000 and B_cnt > 0:
        res = "No"
    else:
        if A_price + B_price < 50000 and C_cnt > 0:
            res = "No"
        elif C_cnt > 1:
            res = "No"

    print(res)

def main():
    A, B, C = read_str()

    menu_A = defaultdict(int)
    menu_B = defaultdict(int)
    menu_C = []

    for _ in range(int(A)):
        name, price = read_str()
        menu_A[name] = int(price)

    for _ in range(int(B)):
        name, price = read_str()
        menu_B[name] = int(price)

    for _ in range(int(C)):
        name = sys.stdin.readline().rstrip()
        menu_C.append(name)

    solve(menu_A, menu_B, menu_C)

if __name__ == "__main__":
    main()