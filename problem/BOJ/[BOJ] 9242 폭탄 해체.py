import sys

emptyCheckArr = []
typeCheckArr = [['*'] * 3 for _ in range(5)]
inputArr = [sys.stdin.readline() for _ in range(5)]
ansArr = []
checker = 0
boom = False

for j in range(len(inputArr[0])):
  if boom:
    break
  else:
    for i in range(5):
      breakIndex = j % 4
      if breakIndex == 3:
        if checker == 2:
          if inputArr[1][j-2] == ' ' and inputArr[3][j-2] == ' ':
            ansArr.append(8)
          else: 
            boom = True
            break
        elif checker == 3:
          if inputArr[2][j - 2]== ' ' and inputArr[1][j-2] == ' ' and inputArr[3][j-2] == ' ':
            ansArr.append(0)
          elif inputArr[1][j-2]== ' ' and inputArr[1][j-1] == ' ' and inputArr[3][j-2] == ' ':
            ansArr.append(6)
          elif inputArr[1][j-2]== ' ' and inputArr[3][j-3] == ' ' and inputArr[3][j-2] == ' ':
            ansArr.append(9)
          else: 
            boom = True
            break
        elif checker == 4:
          if inputArr[1][j-3] == ' ' and inputArr[1][j-2] == ' ' and inputArr[3][j-2]== ' ' and inputArr[3][j-1] == ' ':
            ansArr.append(2)
          elif inputArr[1][j-2] == ' ' and inputArr[1][j-1] == ' ' and inputArr[3][j-3] == ' ' and inputArr[3][j-2] == ' ':
            ansArr.append(5)
          elif inputArr[1][j-3] == ' ' and inputArr[1][j-2] == ' ' and inputArr[3][j-3] == ' ' and inputArr[3][j-2] == ' ':
            ansArr.append(3)
          else: 
            boom = True
            break
        elif checker == 6:
          if inputArr[0][j-2] == ' ' and inputArr[1][j-2] == ' ' and inputArr[3][j-3] == ' ' and inputArr[3][j-2] == ' ' and inputArr[4][j-2] == ' ' and inputArr[4][j-3] == ' ':
            ansArr.append(4)
          else: 
            boom = True
            break
        elif checker == 8:
          if inputArr[1][j-2] == ' ' and inputArr[1][j-3] == ' ' and inputArr[2][j-3] == ' ' and inputArr[2][j-3] == ' ' and inputArr[3][j-2] == ' ' and inputArr[3][j-3] == ' ' and inputArr[4][j-3] == ' ' and inputArr[4][j-2] == ' ':
            ansArr.append(7)
          else: 
            boom = True
            break
        elif checker == 10:
          if inputArr[0][j-1] == '*' and inputArr[1][j-1] == '*' and inputArr[2][j-1] == '*' and inputArr[3][j-1] == '*' and inputArr[4][j-1] == '*':
            ansArr.append(1)
          else: 
            boom = True
            break
        else:
          boom = True
        checker = 0
        break
      else:
        if inputArr[i][j] == ' ':
          checker+=1

if boom:
  print('BOOM!!')
else:
  number = ''
  for word in ansArr:
    number += str(word)
  if int(number) % 6 == 0:
    print('BEER!!')
  else:
    print('BOOM!!')