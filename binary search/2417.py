#백준 2417 실4 15분 //
import sys
input = sys.stdin.readline

def binary_search(n):
    l = 0
    r = n

    while l <= r:
        mid = (l + r) // 2

        if mid * mid >= n:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1

    return ans

def main():
    n = int(input())

    print(binary_search(n))

if __name__ == "__main__":
    main()

"""
def binary_search(n):
    l = 0
    r = n

    while l <= r:
        mid = (l + r) // 2

        if mid * mid < n:
            l = mid + 1
        else:
            r = mid - 1

    return l

def main():
    n = int(input())

    print(binary_search(n))

if __name__ == "__main__":
    main()
"""