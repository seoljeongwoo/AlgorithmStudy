import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().rstrip('\n').split())
edge = [ [] for _ in range(N+1)]
inq = [0]*(N+1)
for Pd in range(M):
    lst = list(map(int,input().rstrip('\n').split()))
    for iter in range(1,lst[0]):
        prevSinger , currSinger = lst[iter] , lst[iter+1]
        edge[prevSinger].append(currSinger)
        inq[currSinger] += 1

que = deque()
for iter in range(1,N+1):
    if inq[iter] == 0:
        que.append(iter)

result = []
while que:
    curr = que.popleft()
    result.append(curr)
    for nx in edge[curr]:
        inq[nx] -= 1
        if inq[nx] == 0: 
            que.append(nx)

if len(result) == N:
    for data in result:
        print(data)
else:
    print(0)

