#!/usr/bin/python3

solutions = [0] * 1000001

def calculate_cycle_length(num):
    print(num)

    if lengths[num] != 0:
        return lengths[num]

    if num == 1:
        val = 1
    elif num % 2 == 1:
        val = 1 + calculate_cycle_length(3 * num + 1)
    else:
        val = 1 + calculate_cycle_length(num // 2)

    lengths[num] = val
    return val

while True:
    try:
        line = input()
        i, j = map(int, line.split())

        max_len = 0
        for n in range(i,j+1, 1):
            max_len = max(calculate_cycle_length(n), max_len)

        # print(str(i) + " " + str(j) + " " + str(max_len))
        print(i, j, max_len)

    except EOFError:
        break