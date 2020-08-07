def checkAbundant(n):

    count = 0
    factors = []

    for i in range(1,n):
        if (n%i == 0):
            count = count + 1
            factors.append(i)

    print("{} --> These are proper divisors of number {}".format(factors,n))

    if (sum(factors) >= n):
        print("{} --> is an abundant number".format(n))
        print("{} --> is the abundance as a result of sum of factors - actual number i.e ({} - {})".format((sum(factors) - n), sum(factors), n))
    else:
        print("{} --> is not an abundant number".format(n))


checkAbundant(24)