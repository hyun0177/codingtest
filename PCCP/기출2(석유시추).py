# PCCP기출 2번 /석유시추 lv2  => 46분 소요  bfs

def solution(land):
    n, m = len(land), len(land[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False for _ in range(m)] for _ in range(n)]
    num = 2
    size_dict = dict()

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                q = [(i, j)]
                visited[i][j] = True
                size = 0

                while q:
                    x, y = q.pop()
                    land[x][y] = num
                    size += 1
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))

                size_dict[num] = size
                num += 1

    ans = 0
    for i in range(m):
        cand = set()
        for j in range(n):
            if land[j][i] != 0:
                cand.add(land[j][i])
        ans = max(ans, sum([size_dict[x] for x in cand]))

    return ans