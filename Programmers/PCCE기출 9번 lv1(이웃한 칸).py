#PCCE기출 9번 lv1(이웃한 칸) 7분 소요

board = [["blue", "red", "orange", "red"],
         ["red", "red", "blue", "orange"],
         ["blue", "orange", "red", "red"],
         ["orange", "orange", "red", "blue"]
         ]
h = 1
w = 1

def solution(board, h, w):
    n = len(board)
    answer = 0

    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]

    for d in range(4):
        nh = h + dh[d]
        nw = w + dw[d]
        if 0 <= nh < n and 0 <= nw < n:
            if board[h][w] == board[nh][nw]:
                answer += 1

    return answer

print(solution(board, h, w))