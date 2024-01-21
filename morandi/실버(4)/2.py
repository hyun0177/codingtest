import sys

n = int(input())

level = list(map(int, sys.stdin.readline().rstrip().split(' ')))
level.sort(reverse=True)

sum = 0
for i in range(len(level)-1):
    i = 0
    sum += level[i] + level[i+1]
    del level[i+1]

print(sum)