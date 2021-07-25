import sys

word = list(sys.stdin.readline().rstrip())

half = int(len(word)/2)
length = int(len(word)) - 1

palindrome = 1

for i in range(0,half):
  if word[i] != word[length - i]:
    palindrome = 0
    break

print(palindrome)