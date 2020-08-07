def ugly_number(n):
    factors = []
    prime_factor = []
    ugly_primes = []
    for i in range(1,n+1):
        if (n%i) == 0:
            factors.append(i)
    for x in factors:
        count = 0
        for i in range(1,x+1):
            if (x%i == 0):
                count = count + 1
        if (count == 2 ):
            prime_factor.append(x)
    for a in prime_factor:
        if (a > 5):
            ugly_primes.append(a)
    if (len(ugly_primes) > 0):
        print("{} --> is not an ugly number".format(n))
    else:
        print("{} --> is an ugly number".format(n))


ugly_number(235)