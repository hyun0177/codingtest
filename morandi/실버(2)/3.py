#***누적합
import sys
input = sys.stdin.readline

N,K,B = map(int,input().split())

arr = [ 0 for _ in range(N+1)]

for i in range(B):
    arr[int(input())] = 1

s=[]
cnt = 0
for i in range(N+1):
    cnt += arr[i]
    s.append(cnt)

answer = B
for i in range(N+1-K):
    answer = min(answer,s[i+K] - s[i])

print(answer)
