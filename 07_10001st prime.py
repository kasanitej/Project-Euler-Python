from math import log
number=10001

limit = number * (log(number) + log(log(number))) #Rosser's Theorem

a = [True] * int(limit)
a[0] = a[1] = False
for (i, isprime) in enumerate(a):
    if i%2 == 0 and i != 2:
        a[i]=False
    if isprime:
        for n in range(i*i,int(limit),i):
            a[n]=False
prime=[i for (i,isprime) in enumerate(a) if isprime]
print(prime)