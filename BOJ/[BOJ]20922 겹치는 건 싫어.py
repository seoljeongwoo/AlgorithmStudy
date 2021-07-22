import sys
input = sys.stdin.readline

N,K = map(int,input().rstrip('\n').split())
lst = list(map(int,input().rstrip('\n').split()))
cnt = [0]*(max(lst)+1)

lp,rp,ret=0,0,0
while rp < N:
    if cnt[lst[rp]] < K:
        cnt[lst[rp]] += 1
        rp +=1
    else:
        ret = max(ret, rp-lp)
        cnt[lst[lp]] -= 1
        lp +=1
ret = max(ret, rp-lp)
print(ret)