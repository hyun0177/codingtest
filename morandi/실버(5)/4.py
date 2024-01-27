#악보는 거들 뿐
import sys
input = sys.stdin.readline

M = int(input())
pList = list(map(int, input().rstrip().split()))

mode = 1
cnt = 1
ans = 1

for i in range(1, M):
    if pList[i] < pList[i - 1]:
        if mode == 0:
            cnt += 1
        else:
            mode = 0
            cnt = 2

    elif pList[i] > pList[i - 1]:
        if mode == 1:
            cnt += 1
        else:
            mode = 1
            cnt = 2

    ans = max(ans, cnt)

print(ans)