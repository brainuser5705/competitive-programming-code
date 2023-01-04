def get_all_pairs(num):
    pairs = []
    for i in range(1, num+1):
        for j in range(i+1, num+1):
            pairs.append([i,j])

    return pairs

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]

    count = 0
    pairs = get_all_pairs(N)
    for pair in pairs:
        all_correct = True
        for i in range(M):
            if not(S[pair[0]-1][i] == 'o' or S[pair[1]-1][i] == 'o'):
                all_correct = False
        if all_correct:
            count += 1
    
    print(count)
        
if __name__ == '__main__':
    main()