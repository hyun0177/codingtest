# 백준 2146 bfs 골3 57분 소요 // bfs 2번 사용

#sol
#1. island_checknum() bfs를 이용해서 각각의 섬에 해당하는 번호로 라벨링하기
#2. 라벨링된 num을 기준으로 bfs를 한번 더 이용해서 라벨링 넘버가 바뀌는 구간을 ans로 설정하고 min값을 갱신해 가며 최종 값 도출

import sys
from collections import deque
read_ints = lambda : list(map(int, sys.stdin.readline().rstrip().split(' ')))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
ans = 1e9

def is_vaild_xy(N, x, y):
    return 0 <= x < N and 0 <= y < N

def island_checknum(N, x, y, map, visited, num):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if is_vaild_xy(N, nx, ny) and not visited[nx][ny] and map[nx][ny]:
                visited[nx][ny] = True
                map[nx][ny] = num
                q.append((nx, ny))

def dist(N, num, map):
    global ans

    visited = [ [-1 for _ in range(N)] for _ in range(N) ]
    q = deque()

    for i in range(N):
        for j in range(N):
            if map[i][j] == num:
                q.append((i, j))
                visited[i][j] = 0

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if is_vaild_xy(N, nx, ny):
                if map[nx][ny] > 0 and map[nx][ny] != num:
                    ans = min(ans, visited[x][y])
                    return
                if map[nx][ny] == 0 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
def solve(N, map):
    global ans

    visited = [ [ 0 for _ in range(N)] for _ in range(N) ]
    num = 1

    for i in range(N):
        for j in range(N):
            if map[i][j] and not visited[i][j]:
                visited[i][j] = True
                map[i][j] = num
                island_checknum(N, i, j, map, visited, num)
                num += 1

    for i in range(1, num):
        dist(N, i, map)

    print(ans)

def main():
    N = int(input())
    map = [ read_ints() for _ in range(N) ]

    solve(N, map)

if __name__ == "__main__":
    main()
