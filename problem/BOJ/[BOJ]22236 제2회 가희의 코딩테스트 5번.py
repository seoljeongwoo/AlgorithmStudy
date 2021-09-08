import sys,heapq
input = sys.stdin.readline

h,m,s = map(int,input().rstrip('\n').split(':'))
arrive_time = h*3600 + m*60 + s
N = int(input())
metro = [2]*300
metro[210] = metro[225] = metro[256] = metro[222] = metro[238] = metro[250] = metro[266] = 3
metro[221] = metro[245] = metro[249] = metro[220] = 4
metro[247] = 5

INF = int(1e9)
dist = [ [] for _ in range(300)]
for i in range(210, 273): 
    heapq.heappush(dist[i], INF)
for _ in range(N):
    lst = list(input().rstrip('\n').split(' '))
    lst[0] = int(lst[0][1:])
    lst[1] = int(lst[1][1:])
    hh,mm = int(lst[2][0:2]) , int(lst[2][3:])
    art_time = hh*3600 + mm*60
    for j in range(lst[0], lst[1]):
        heapq.heappush(dist[j], art_time)
        art_time += metro[j]*60 + 20
for j in range(225, 272):
    while dist[j] and dist[j][0] < arrive_time:
        heapq.heappop(dist[j])
    if len(dist[j]) != 0 :arrive_time = dist[j][0]
    arrive_time += metro[j]*60 + 20
arrive_time -= 20
if arrive_time <= 23*3600 + 59*60 + 59:
    ret = ''
    hh = arrive_time // 3600
    arrive_time %= 3600
    mm = arrive_time // 60
    arrive_time %= 60
    ss = arrive_time
    if hh < 10: ret += '0'
    ret += str(hh) + ':'
    if mm < 10 : ret += '0'
    ret += str(mm) + ':'
    if ss < 10: ret += '0'
    ret += str(ss)
    print(ret)
else:
    print(-1)

