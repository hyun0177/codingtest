# 백준 21317 *** 58분 징검다리 건너기 // dp 2개 사용 =>
# case1 마지막이 큰 점프로 끝나는 케이스
# case2 마지막이 작은 점프로 끝나는 케이스
# case3 마지막이 매우 큰 점프로 끝나는 케이스
#촤종 점화식
# => case1, case2 만 적용 dp[i]=min(mlist[i-1][0]+dp[i-1], mlist[i-2][1]+dp[i-2])
# => case 3 확인 - > dp2[j]=min(dp[j], dp2[j-1]+mlist[j-1][0], dp2[j-2]+mlist[j-2][1])

n=int(input())
mlist=[[0]*2 for _ in range(n-1)]
for i in range(n-1):
    a, b=map(int,input().split())

    mlist[i][0]=a
    mlist[i][1]=b

k=int(input())

if n==1:
    print(0)
    exit()
elif n==2:
    print(mlist[0][0])
    exit()
dp=[0]*n

dp[1]=mlist[0][0]
dp[2]=min(mlist[0][0]+mlist[1][0], mlist[0][1])

for i in range(3, n):
    dp[i]=min(mlist[i-1][0]+dp[i-1], mlist[i-2][1]+dp[i-2])

res=dp[-1]
dp2=dp[:]

for i in range(0, n-3):
    if dp[i]+k<dp[i+3]:
        dp2[i+3]=dp[i]+k
        for j in range(i+4, n):
            dp2[j]=min(dp[j], dp2[j-1]+mlist[j-1][0], dp2[j-2]+mlist[j-2][1])
        if dp2[-1]<res:
            res=dp2[-1]
print(res)