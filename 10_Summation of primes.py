Number=2000000
a=[True]*Number
a[0]=a[1]=False
for (i,isprime) in enumerate(a):
    if i%2 ==0 and i!=2:
        a[i]=False
    if isprime:
        for num in range(i*i,Number,i):
            a[num]=False

from functools  import reduce
prime=[i for (i,isprime) in enumerate(a) if isprime]
print(reduce(lambda x,y:x+y,prime))
