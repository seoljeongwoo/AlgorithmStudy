import sys
input = sys.stdin.readline
sys.setrecursionlimit(100005)

N = int(input())
edge = [ [] for _ in range(N+1)]
parent = [-1] * (N+1)
for _ in range(N-1):
    u,v = map(int,input().rstrip('\n').split())
    edge[u].append(v)
    edge[v].append(u)
def solve(curr, pa):
    global parent
    parent[curr] = pa
    for next_vertex in edge[curr]:
        if parent[next_vertex] == -1:
            solve(next_vertex, curr)
    return
solve(1,0)
for pa in range(2,N+1):
    print(parent[pa])


