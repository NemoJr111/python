def sum(a, b):
    c = a+b
    d = a-b
    e = a*b 
    f = a/b 
    return c, d, e, f 

a = int(input('enter a: '))
b = int(input('enter b: '))

p, q, r, rt = sum(a, b)

print('\nsum= ', p)
print('Sub= ', q)
print('mul= ', r)
print('div= ', rt)
