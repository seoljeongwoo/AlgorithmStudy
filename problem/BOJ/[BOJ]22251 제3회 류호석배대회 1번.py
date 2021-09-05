import sys
input = sys.stdin.readline

N,K,P,X = map(int,input().split())
answer = 0
convert = { 0 : [0,4,3,3,4,3,2,3,1,2] ,
            1 : [4,0,5,3,2,5,6,1,5,4] ,
            2 : [3,5,0,2,5,4,3,4,2,3] ,
            3 : [3,3,2,0,3,2,3,2,2,1] ,
            4 : [4,2,5,3,0,3,4,3,3,2] ,
            5 : [3,5,4,2,3,0,1,4,2,1] ,
            6 : [2,6,3,3,4,1,0,5,1,2] ,
            7 : [3,1,4,2,3,4,5,0,4,3] ,
            8 : [1,5,2,2,3,2,1,4,0,1] ,
            9 : [2,4,3,1,2,1,2,3,1,0]
            }
def con(v):
    global N
    temp = v
    ret = []
    while temp:
        ret.append(temp%10)
        temp//=10
    while len(ret) < K:
        ret.append(0)
    ret.reverse()
    return ret

def judge(goal):
    global convert
    lst , llst = con(X), con(goal)
    ret = 0
    for i in range(K):
        ret += convert[lst[i]][llst[i]]
    return True if ret >0 and ret <= P else False

for i in range(1,N+1):
    if judge(i): 
        answer +=1
print(answer)
