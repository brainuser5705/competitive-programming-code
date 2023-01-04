N = int(input())
S = list(input())

enclosed = False
for i in range(N):
    if S[i] == '"':
        enclosed = not enclosed
    elif not enclosed and S[i] == ',':
        S[i] = '.'

print(''.join(S))