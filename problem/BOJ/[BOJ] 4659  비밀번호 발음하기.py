import sys

vArr = 'aeiou'

while True:
  co = 0
  vo = 0
  answer = False
  vCheck = False
  bre = False
  p = list(map(str,sys.stdin.readline().rstrip()))
  if ''.join(p) == 'end':
    break

  for i in range(len(p)):
    if i != 0 and p[i] == p[i-1]:
      if p[i] != 'e' and p[i] != 'o':
        bre = True
        break

    if vo >=3 or co >=3:
      bre = True
      break
      
    if vArr.find(p[i]) == -1:
      co += 1
      vo = 0
    else:
      vCheck = True
      vo += 1
      co = 0  
  
  if vo >=3 or co >=3:
    bre = True

  if bre or vCheck == False:
    print('<%s> is not acceptable.' %(''.join(p)))
  else:
    print('<%s> is acceptable.' %(''.join(p)))

## regex로 풀면 될것같지만.. 잘모르겠어서 if문으로 문제를 품.
## regex 공부하자!

