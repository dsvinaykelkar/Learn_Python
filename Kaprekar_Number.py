def checkKaprekar(n):

    digits = []
    largest = []
    smallest = []
    large = 0
    small = 0
    sub=0
    temp = str(n)
    num = n

    for i in range(1,8):

        for i in range(len(temp)):
            digits.append(int(temp[i]))

        largest = sorted(digits,reverse=True)
        smallest = sorted(digits,reverse=False)
        print("{} --> largest number that can be made out of given number {}".format(largest,n))
        print("{} --> smallest number that can be made out of given number {}".format(smallest,n))
        large = int("".join(map(str,largest)))
        small = int("".join(map(str,smallest)))
    
        if ((large - small) == 6174 ) :
             print("{} --> is Kparekar number guys".format(num))
             return
        else:
            sub = large - small
            print("There difference is {}".format(sub))
            print("-------------------------------------------------------------")
            temp = str(sub)
            digits = []
            n = sub
            


checkKaprekar(7652)
