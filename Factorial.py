def factorial(n):
    fact=1
    sum=0
    for i in reversed(range(1,n+1)):
        print(i)
        sum = fact * i
        fact = sum
    print("The factorial of number {} is {} ".format(n,fact))

factorial(5)