import sys
input = sys.stdin.readline

N,Q = map(int,input().rstrip('\n').split())
array = [0]*(N+1)
for _ in range(Q):
    goal = int(input())
    path = []
    while goal:
        path.append(goal)
        goal//=2
    ret = 0
    for data in path[::-1]:
        if array[data] != 0:
            ret = data
            break
    if ret == 0:
        print(0)
        array[path[0]] = 1
    else:
        print(ret)
    