def prime(z):
    cnt=0
    divisors=[]
    for i in range(1,z+1):
        if (z%i) == 0:
            cnt = cnt + 1
            divisors.append(i)
    print("Total number of divisors: ", cnt)
    print("The divisors are : ",divisors)
    if(cnt == 2):
        print("{} is a prime number".format(z))
    else:
        print("{} is not a prime number".format(z))


prime(17)