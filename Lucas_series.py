def seriesLucas(n):
    a = 2
    b = 1
    temp = a+b
    swap = 0
    lucas = [2,1]

    if (n == 1):
        print("{} --> This is very first Number of Lucas Series".format(lucas[n-1]))
    
    elif (n == 2):
        print("{} --> These are first {} Numbers of Lucas Series".format(lucas,n))
    
    elif ( n > 2):
        for _ in range(n-2):
            swap = temp
            lucas.append(swap)
            temp = swap + b 
            b = swap
        print("{} --> These are first {} Numbers of Lucas series".format(lucas,n))


seriesLucas(4)
