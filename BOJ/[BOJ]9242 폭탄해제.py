import sys
input = sys.stdin.readline

zeroNumber = ['***','* *','* *','* *','***']
oneNumber = ['  *','  *','  *','  *','  *']
twoNumber = ['***','  *','***','*  ','***']
threeNumber = ['***','  *','***','  *','***']
fourNumber = ['* *','* *','***','  *','  *']
fiveNumber = ['***','*  ','***','  *','***']
sixNumber = ['***','*  ','***','* *','***']
sevenNumber = ['***','  *','  *','  *','  *']
eightNumber = ['***','* *','***','* *','***']
nineNumber = ['***','* *','***','  *','***']

number = []
number.append(zeroNumber)
number.append(oneNumber)
number.append(twoNumber)
number.append(threeNumber)
number.append(fourNumber)
number.append(fiveNumber)
number.append(sixNumber)
number.append(sevenNumber)
number.append(eightNumber)
number.append(nineNumber)

code = []
for row in range(5):
    col = input().rstrip('\n')
    code.append(col)

result = True
codeNumber = 0
size = len(code[0])

for start in range(0,size,4):
    if start + 2 >= size :
        result = False
        break
    correctCount = 0
    for numberCheck in range(10):
        isSame = True
        for x in range(5):
            for y in range(3):
                if number[numberCheck][x][y] != code[x][y + start]:
                    isSame = False
        if isSame == True:
            codeNumber = codeNumber * 10 + numberCheck
            correctCount += 1
            break
    if correctCount == 0 :
        result = False

print("BEER!!" if result == True and codeNumber % 6 == 0 else "BOOM!!")

'''
문자로 이루어진 숫자를 추출하는 방법이 어려웠음.
직접 숫자에 해당하는 문자를 미리 집어넣지않고 해결할수 있을까?
'''
