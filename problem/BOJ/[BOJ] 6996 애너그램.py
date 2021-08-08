import sys

case = int(sys.stdin.readline().rstrip())
answer = False

for _ in range(case):
  F,B = map(str,sys.stdin.readline().split())
  if len(F) != len(B):
    answer = True
  else:
    if sorted(F) != sorted(B):
      answer = True
  if(answer):
    print('%s & %s are NOT anagrams.' %(F,B))
  else:
    print('%s & %s are anagrams.' %(F,B))

  answer = False

## 리스트 비교는 == 으로 가능하다.
## sorted 는 sort된 리스트를 출력한다.
