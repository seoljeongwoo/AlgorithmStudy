import sys, heapq
input = sys.stdin.readline

info = dict()
Q = int(input())
answer = 0
for q in range(Q):
    lst = list(input().rstrip('\n').split())
    if lst[0] == '1':
        id , cnt = lst[1], int(lst[2])
        if id not in info.keys():
            info[id] = []
        for i in range(cnt):
            heapq.heappush(info[id], -1*int(lst[3+i]))
    else:
        id , cnt = lst[1], int(lst[2])
        if id not in info.keys(): continue
        for i in range(min(cnt, len(info[id]))):
            answer -= heapq.heappop(info[id])
print(answer)