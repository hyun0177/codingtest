# 백준 14502 골5 45분

import sys
import copy

read_ints = lambda : list(map(int, sys.stdin.readline().rstrip().split(' ')))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def wall_construct(wall_cnt):
    if wall_cnt == 3:
        virus_spread()
        return
    for n in range(N):
        for m in range(M):
            if board[n][m] == 0:
                board[n][m] = 1
                wall_construct(wall_cnt + 1)
                board[n][m] = 0

def virus_spread():
    global answer
    board_wall = copy.deepcopy(board)


    virus = [(n, m) for n in range(N) for m in range(M) if board_wall[n][m] == 2]

    while virus:
        x, y = virus.pop()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and board_wall[nx][ny] == 0:
                board_wall[nx][ny] = 2
                virus.append((nx, ny))

    safe_cnt = 0
    for b in board_wall:
        safe_cnt += b.count(0)
    answer = max(answer, safe_cnt)

if __name__ == "__main__":
    N, M = read_ints()
    board = [ read_ints() for _ in range(N)]
    answer = 0
    wall_construct(0)

    print(answer)