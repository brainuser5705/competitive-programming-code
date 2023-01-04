k = int(input())

c = 1
val = 1
while val % k != 0:
    c += 1
    val *= c

print(c)