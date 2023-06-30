import random

num = random.randint(1,100)

def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False

    return True

print(num)
print(is_prime(num))