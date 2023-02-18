import math


def isPrime(n):
    if n == 2 or n == 3:
        return True
    elif n > 2:
        for i in range(2, round(math.sqrt(n))+1):
            if n % i == 0:
                return False
        else:
            return True
    else:
        return False


def xthPrimeNumber(x):
    w = 1
    primesBefore = 0
    while primesBefore != x:
        if isPrime(w):
            primesBefore += 1
        w += 1
    return w - 1


def isPrimeLaborious(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True


xth_prime_number = xthPrimeNumber(100000)
print(xth_prime_number)
print(isPrimeLaborious(xth_prime_number))
