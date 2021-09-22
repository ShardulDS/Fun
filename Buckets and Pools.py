'''You are in charge of filling up a swimming pool with a capacity of C litres. You can use a
bucket which can fill at most B litres.
Write clean and efficient Python code to find the total number of ways to fill up the
swimming pool using that bucket. You cannot use a bucket with 0 litres to fill, i.e, the
litres of water in the bucket should be positive integers.'''


def factorial(x):
    if x == 1:
        return 1
    else:
        return x*factorial(x-1)


def ncr (n, r):
    return factorial(n)//(factorial(n-r)*factorial(r))


def main(c, b):
    ways = 0
    min_terms = c//b
    if c%b != 0:
        min_terms += 1
    for i in range(min_terms, c+1):
        ways += ncr(c-1, i-1)
    return ways
    

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        c, b = [int(k) for k in input().split()]
        print(main(c, b))
