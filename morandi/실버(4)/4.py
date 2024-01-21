from collections import deque

N, M, K = 0, 0, 0
MAP = [[]]
Visited = [[]]
MoveY = [-1, 0, 1, 0]
MoveX = [0, -1, 0, 1]
Answer = 0

def input_data():
    global N, M, K, MAP
    N, M, K = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]

def bfs(Y, X):
    global Visited
    Q = deque([(Y, X)])
    Visited[Y][X] = True
    R = 0

    while Q:
        NowY, NowX = Q.popleft()
        R += 1

        for i in range(4):
            NextY, NextX = NowY + MoveY[i], NowX + MoveX[i]
            if 0 <= NextY < N and 0 <= NextX < N and not Visited[NextY][NextX] and MAP[NextY][NextX] == 0:
                Visited[NextY][NextX] = True
                Q.append((NextY, NextX))

    return R

def settings():
    global Answer, Visited
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 0 and not Visited[i][j]:
                R = bfs(i, j)
                Answer += (R // K) + (1 if R % K != 0 else 0)

def find_answer():
    global Answer
    if Answer >= 1:
        if M >= Answer:
            for i in range(N):
                for j in range(N):
                    if MAP[i][j] == 0 and not Visited[i][j]:
                        print("IMPOSSIBLE")
                        return
            print("POSSIBLE")
            print(M - Answer)
        else:
            print("IMPOSSIBLE")
    else:
        print("IMPOSSIBLE")

def main():
    global N, M, K, MAP, Visited, Answer
    input_data()
    Visited = [[False] * N for _ in range(N)]
    settings()
    find_answer()

if __name__ == "__main__":
    main()