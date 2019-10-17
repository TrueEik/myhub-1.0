def func(x):
    if (x>1):
        for i in range(2, x):
            a = x%i
            if (a==0):
                print('This is not a Prime number')
                break
            else:
                print('This is a Prime number')
    else:
        print('This is not a Prime number') 
