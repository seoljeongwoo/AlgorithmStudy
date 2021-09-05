import sys
input = sys.stdin.readline

N = int(input())
day , point = [], []
for _ in range(N):
    d, p = map(int,input().split())
    day.append(d)
    point.append(p)
flag = [False] * N
ret = 0
for d in range(max(day) , 0, -1):
    pick = -1
    for i in range(N):
        if flag[i] == False and day[i] >= d:
            if pick == -1: pick = i
            else: pick = pick if point[pick] >= point[i] else i
    print(pick)
    if pick != -1:
        flag[pick] = True
        ret += point[pick]
print(ret)
