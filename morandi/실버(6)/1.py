# 성적표
def solution():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    min_rss = float('inf')
    min_a, min_b = 0, 0

    for a in range(1, 101):
        for b in range(1, 101):
            rss = 0
            for i in range(n):
                cur = arr[i][0] * a + b - arr[i][1]
                rss += cur * cur

            if min_rss > rss:
                min_rss = rss
                min_a = a
                min_b = b

    print(min_a, min_b)

if __name__ == "__main__":
    solution()