import sys
input = sys.stdin.readline
N,M = map(int,input().rstrip('\n').split())
train = [0]*N
for query in range(M):
    lst = list(map(int,input().rstrip('\n').split()))
    if lst[0] == 1:
        i , x = lst[1]-1, lst[2]-1  
        train[i] |= (1<<x)
    elif lst[0] == 2:
        i , x = lst[1]-1, lst[2]-1
        train[i] &= ~(1<<x)
    elif lst[0] == 3:
        i = lst[1] -1
        train[i] = (train[i] << 1)
        train[i] &= ~(1<<20)
    else:
        i = lst[1] -1
        train[i] = (train[i] >> 1)
print(len(set(train)))