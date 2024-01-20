# 풀이 실패 - 예제 정답은 맞게 출력했으나 4%에서 실패

import sys

read_str = lambda : list(map(str, sys.stdin.readline().rstrip()))
read_ints = lambda : list(map(int, sys.stdin.readline().rstrip().split(' ')))

def solve(N, M, board):
    res = []
    cnt = 1
    for i in range(N):
        for j in range(M):
            if board[i][j] != '#':
                # 가로 단서인 경우
                if (j == 0 or board[i][j-1] == '#') and (j < M-2 and board[i][j+2] == '.'):
                    board[i][j] = cnt
                    res.append((i+1, j+1))
                    cnt += 1
                # 세로 단서인 경우
                elif (i == 0 or board[i-1][j] == '#') and (i < N-2 and board[i+2][j] == '.'):
                    board[i][j] = cnt
                    res.append((i+1, j+1))
                    cnt += 1

    print(len(res))
    for r in res:
        print(f"{r[0]}{r[1]}")

def main():
    N, M = read_ints()
    board = [ read_str() for _ in range(N) ]

    solve(N, M, board)

if __name__ == "__main__":
    main()