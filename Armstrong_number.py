def armstrong(n):
    sum = 0
    n_to_str = str(n)
    n_list = []
    no_of_digits = len(n_to_str)
    for i in range(0,no_of_digits):
        n_list.append(n_to_str[i])
    print("{} --> individual digits of the number --> {}".format(n_list,n))
    for j in n_list:
        sum = sum + int(j)**no_of_digits
    print("{} --> is the of value after doing each digit to the power of no of digits --> {}".format(sum,n))    
    if (sum == n):
        print("{} --> is an Armstrong number".format(n))
    else:
        print("{} --> is not an Armstrong number".format(n))

armstrong(153)