def SieveOfEratosthenes(n):
      
    # Create a boolean array "prime[0..n]" and
    # initialize all entries it as true. A value
    # in prime[i] will finally be false if i is
    # Not a prime, else true.
    prime = [True for i in range(n+1)]
     
    p = 2
    while(p * p <= n):
          
        # If prime[p] is not changed, then it is
       # a prime
        if (prime[p] == True):
              
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return prime

def reduction(n):
    primes = SieveOfEratosthenes(n)
    primeFacs = []
    for i in reversed(range(n)):
        if primes[i]:
            primeFacs.append(i)
    return len(primeFacs)

if __name__ == '__main__':
    n = int(input())
    print(reduction(n))    
