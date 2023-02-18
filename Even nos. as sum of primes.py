"""Every even number can be expressed as sum of two primes. Find the two primes."""
import numpy as np
n = 2000

def is_prime(x):
    if x == 1:
        return True
    elif x < 1:
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        else:
            return True


def primes_sum(a):
    lst = np.empty((0, 2), int)
    if is_prime(a // 2):
        lst = np.append(lst, np.array([[a//2, a//2]]), axis=0)
    for i in reversed(range(a // 2)):
        if is_prime(i) and is_prime(a - i):
            lst = np.append(lst, np.array([[i, a-i]]), axis=0)
    return lst


for operands in primes_sum(n):
    print(operands[0], '+', operands[1], '=', n)