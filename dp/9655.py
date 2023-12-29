# 백준 9655 dp

#sol1) N의 값이 홀, 짝, 홀, 짝 이냐에 따라 승패가 갈린다. 31120KB , 40ms

"""
import sys

N = int(sys.stdin.readline())

if N % 2 == 0: print("CY")
else: print("SK")
"""

#sol2) dp에 저장할 값은 턴의 수로 계산해서 저장한다. 턴이 홀수면 SK, 짝수면 CY
# 31252KB, 40ms // 출력 해야되는 값의 타입에 따라 dp에 넣는 타입도 맞춰서 저장하자.
"""
import sys

N= int(sys.stdin.readline());

dp = ['' for _ in range(1001)]

dp[1] = 'SK'

for i in range(1, 1000):
    if dp[i] == 'SK':
        if dp[i+1] == '':
            dp[i+1] = 'CY'
        if i + 3 < 1001:
            dp[i+3] = 'CY'
    elif dp[i] == 'CY':
        if dp[i+1] == '':
            dp[i+1] = 'SK'
        if i + 3 < 1001:
            dp[i+3] = 'SK'

print(dp[N])
"""