s = input()
t = input()

for i in range(len(s)):
    if s[i] != t[i]:
        print(i+1)
        break

if (i+1) == len(s): # python doesn't go past the bound
    print(i+2)