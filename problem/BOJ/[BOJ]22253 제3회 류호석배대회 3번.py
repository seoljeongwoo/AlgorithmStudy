import sys
sys.setrecursionlimit(101010)
input = sys.stdin.readline

N = int(input())
p = list(map(int,input().split()))
graph = [ [] for _ in range(N)]
for _ in range(N-1):
    a ,b = map(int,input().rstrip('\n').split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

DP = dict()
MOD = int(1e9) + 7
def solve(curr,par,mv):
    # memo
    key = (curr, mv)
    if key not in DP.keys(): DP[key] = 0
    else: return DP[key]

    for nx in graph[curr]:
        if par == nx :continue
        if mv <= p[nx]:
            DP[key] += solve(nx,curr,p[nx]) + 1
            DP[key] = DP[key]%MOD
        DP[key] += solve(nx,curr,mv)
        DP[key] = DP[key]%MOD
    return DP[key]

answer = solve(0,0,-1) + solve(0,0,p[0]) +1
print(answer%MOD)