def counDigits(n):

    temp = str(n)
    print("{} --> Number of digits in {}".format(len(temp),n))
    digits = []

    for i in range(len(temp)):
        digits.append(temp[i])
    print("{} --> These are digits of number {}".format(digits,n))
counDigits(193)
