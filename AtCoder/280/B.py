size = input()
s = input().split(' ')

print(s[0], end=' ')
for i in range(1,len(s)):
    print(int(s[i])-int(s[i-1]), end=' ')