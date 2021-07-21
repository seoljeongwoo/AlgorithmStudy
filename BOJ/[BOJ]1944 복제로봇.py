import sys
input = sys.stdin.readline

N,M = map(int,input().rstrip('\n').split())
lst = [ list(input().rstrip('\n')) for _ in range(N)]
print(lst)
