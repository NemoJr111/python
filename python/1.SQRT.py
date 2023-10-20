import math
a=float(input('enter a: '))
b=float(input('enter b: '))
c=float(input('enter c: '))
d=(b*b)-(4*a*c)
if d>0:
    r1=(-b+math.sqrt(d))//(2*a)
    r2=(-b-math.sqrt(d))//(2*a)
    print('\nDistinct Roots = ',r1,',',r2)
elif d==0:
    r1=-b//(2*a)
    print('\nEqual Roots = ',r1)
else:
    print('\nComplex Roots')
    print(-b//(2*a),'+i',math.sqrt(abs(d)))
    print(-b//(2*a),'-i',math.sqrt(abs(d)))