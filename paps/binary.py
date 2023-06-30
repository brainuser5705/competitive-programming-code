import random

def construct_array(length):
    curr = random.randint(0,10)
    arr = [curr]

    for _ in range(length):
        curr += random.randint(0,10)
        arr.append(curr)

    return arr

def search_index(arr, num):
    low = 0
    end= len(arr)-1

    while end >= low:
        mid = (end+low) // 2
        guess = arr[mid]
        if guess == num:
            return mid
        elif num < guess:
            end = mid-1
        elif num > guess:
            low = mid+1
        
    return -1

def main():
    arr = construct_array(10)
    real = arr[random.randint(0,len(arr)-1)]
    index = search_index(arr, real)

    print("array:", arr)
    print("real:", real)
    print("index:", index)
    
main()
    
    