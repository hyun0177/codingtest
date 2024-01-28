# 인간-컴퓨터 상호작용
# pypy3 로 제출시 100% python3 으로 제출시 50%
import sys
input = sys.stdin.readline

s = input()
n = int(input())
re = [[0 for _ in range(26)] for _ in range(len(s))]

for i in range(len(s)):
    for j in range(26):
        if ord(s[i]) - 97 == j:
            re[i][j] = re[i-1][j] + 1
        else:
            re[i][j] = re[i-1][j]

for _ in range(n):
    t, x, y = input().split()
    if int(x) == 0:
        print(re[int(y)][ord(t)-97])
    else:
        print(re[int(y)][ord(t)-97] - re[int(x)-1][ord(t)-97])