import sys
read_ints = lambda : list(map(int, sys.stdin.readline().rstrip().split(' ')))

def main():
    N, M = read_ints()
    point = read_ints()
    point.sort()

    for i in range(M):
        l = 0
        r = N - 1
        a, b = read_ints()

        while l <= r:
            mid = (l + r) // 2
            if a > point[mid]:
                l = mid + 1
            else:
                r = mid - 1
        res = r + 1

        l = 0
        r = N - 1

        while l <= r:
            mid = (l + r) // 2
            if b >= point[mid]:
                l = mid + 1
            else:
                r = mid - 1
        res2 = r

        print(res2 - res + 1)

if __name__ == "__main__":
    main()

"""
sol.
다른 사람들 풀이 = > 함수로 만들어서 작성. 
위 풀이와 마찬가지로 입력받은 a, b에 대해서 각각 min max 함수를 따로 만들어서 작성

참고 후 수정 코드

import sys
read_ints = lambda : list(map(int, sys.stdin.readline().rstrip().split(' ')))

def binary_min(l, r, point, target):
    while l <= r:
        mid = (l + r) // 2
        if target > point[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return r + 1

def binary_max(l, r, point, target):
    while l <= r:
        mid = (l + r) // 2
        if target >= point[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return r

def main():
    N, M = read_ints()
    point = read_ints()
    point.sort()

    for i in range(M):
        a, b = read_ints()

        print(binary_max(0, N-1, point, b) - binary_min(0, N-1, point, a) + 1)

if __name__ == "__main__":
    main()
    
"""