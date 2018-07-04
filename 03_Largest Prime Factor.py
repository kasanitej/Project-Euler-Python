#n = 600851475143
n=76576500
i = 2
print('1',end='') 
while i <= n:
    k=0;
    while n%i == 0:
        n = n / i
        k = k + 1
    if k!=0:
        print('*',i,'^',k,end='')
    i = i + 1