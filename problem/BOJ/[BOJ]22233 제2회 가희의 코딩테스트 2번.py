import sys
input = sys.stdin.readline

N,M = map(int,input().rstrip('\n').split())
memo = { input().rstrip('\n') : True for _ in range(N)}
eraser = {}
for query in range(M):
    for data in list(input().rstrip('\n').split(',')):
        if data in eraser.keys(): continue
        if data in memo.keys():
            del memo[data]
            eraser[data] = True
    print(len(memo))
