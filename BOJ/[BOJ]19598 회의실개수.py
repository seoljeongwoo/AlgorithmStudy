import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    st,en = map(int,input().rstrip('\n').split())
    lst.append((st, 1))
    lst.append((en,-1))
lst.sort()
room , ret = 0, 0
for index, data in enumerate(lst):
    room += data[1]
    ret = max(ret,room)
print(ret)