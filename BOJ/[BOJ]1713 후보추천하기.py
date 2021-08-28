import sys
from collections import deque
input = sys.stdin.readline

N , M = int(input()) , int(input())
lst = list(map(int,input().rstrip('\n').split()))
s , c = [], dict()
for data in lst:
    if data in s:
        c[data] +=1
    elif len(s) < N :
        s.append(data)
        c[data] = 1
    else:
        pick = s[0]
        for k in s:
            if c[pick] > c[k]:
                pick = k
        s.remove(pick)
        s.append(data)
        c[data] = 1
print(*sorted(s))