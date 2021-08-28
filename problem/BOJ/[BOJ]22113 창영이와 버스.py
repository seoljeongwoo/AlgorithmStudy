import sys
input = sys.stdin.readline

N,M = map(int,input().rstrip('\n').split())
lst = list(map(int,input().rstrip('\n').split()))
A = [list(map(int,input().rstrip('\n').split())) for _ in range(N)]
ans = 0
for i in range(1,M):
    ans += A[lst[i-1]-1][lst[i]-1]
print(ans)