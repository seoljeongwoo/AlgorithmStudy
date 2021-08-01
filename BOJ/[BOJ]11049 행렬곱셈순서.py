import sys
input = sys.stdin.readline

N = int(input())
metrix = []
DP = [[0]*N for _ in range(N)]
for _ in range(N):
    metrix.append(tuple(map(int,input().rstrip('\n').split())))
for i in range(1,N): # 1 2
    for j in range(N-i): # 0 1
        DP[j][j+i] = (1<<31)
        for k in range(j,j+i):
            DP[j][j+i] = min(DP[j][j+i] , DP[j][k] + DP[k+1][j+i] + metrix[j][0]*metrix[k][1]*metrix[j+i][1])
print(DP[0][N-1])
