#백준 10870 브1,2 => 31120 KB, 40ms

import sys

n = int(sys.stdin.readline())

pibo = [i for i in range(n+1)]

for i in range(2, n+1):
    pibo[i] = pibo[i-1] + pibo[i-2]

print(pibo[n])
