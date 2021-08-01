import sys
input = sys.stdin.readline
l = int(input())
lst = list(map(int,input().rstrip('\n').split()))
n = int(input())
l,r = 1, 1000
for data in lst:
    if data <= n:
        l = max(l, data+1)
    if data >=n:
        r = min(r, data-1)
ret = 0
for i in range(l,r+1):
    for j in range(i+1,r+1):
        if i<= n <=j: 
            ret+=1
print(ret)