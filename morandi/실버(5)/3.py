#dp 자원 캐기
import sys

read_str = lambda : sys.stdin.readline().rstrip()
read_ints = lambda : list(map(int, read_str().split(' ')))
read_int = lambda : read_ints()[0]


def dp_sol(x, y, dp, board):
    if x < 0 or y < 0: return 0
    if dp[x][y] != -1: return dp[x][y]

    dp[x][y] = board[x][y]
    dp[x][y] += max(dp_sol(x-1, y, dp, board), dp_sol(x, y-1, dp, board))

    return dp[x][y]

def solve(N, M, board):
    dp = [ [-1 for _ in range(M)] for _ in range(N) ]
    dp[0][0] = board[0][0]

    print(dp_sol(N-1, M-1, dp, board))

def main():
    N, M = read_ints()

    board = [ read_ints() for _ in range(N) ]

    solve(N, M, board)

if __name__ == "__main__":
    main()