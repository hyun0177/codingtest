# 백준 16234 인구이동 골4 34분

import sys
from collections import deque

read_ints = lambda : list(map(int, sys.stdin.readline().rstrip().split(' ')))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def is_vaild_xy(x, y, n):
    return 0 <= x < n and 0 <= y < n
def bfs(n, l, r, A, i, j, visited):
    q = deque()
    union = []
    q.append((i, j))
    union.append((i, j))

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if is_vaild_xy(nx, ny, n) and visited[nx][ny] == 0:
                if l <= abs(A[nx][ny] - A[x][y]) <= r:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    union.append((nx, ny))
    return union

def solve(n, l, r, A):
    result = 0

    while True:
        visited = [[0 for _ in range(n)] for _ in range(n)]
        flag = 0
        for i in range(n):
            for j in range(n):
                if visited[i][j] == 0:
                    visited[i][j] = 1
                    country = bfs(n, l, r, A, i, j, visited)

                    if len(country) > 1:
                        flag = 1
                        people = sum(A[x][y] for x, y in country) // len(country)

                        for x, y in country:
                            A[x][y] = people
        if flag == 0:
            break
        result += 1

    return result

def main():
    n, l, r = read_ints()
    A = [ read_ints() for _ in range(n)]

    print(solve(n, l, r, A))

if __name__ == "__main__":
    main()