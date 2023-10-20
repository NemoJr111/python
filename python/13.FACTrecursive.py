def fact(x):
    if x==1:
        return 1
    else:
        f = x*fact(x-1)
    return f 

n = int(input("enter the number: "))
f = fact(n) 
print('\nfactorial of ', n, 'is', f)