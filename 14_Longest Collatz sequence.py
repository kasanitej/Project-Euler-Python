num=1000000
a=[-1]*num
a[0]=0

for num1,Cond in enumerate(a):
    if Cond==-1:
        collatz=[]
        n=num1
        collatz.append(int(n));#print('adding link:',n)
        while n>1:
            if n%2==0:
                 n=n/2;#print(int(2*n),'-->',int(n))
                 if num1>n:
                    collatz+=[0]*a[int(n)]
                    break
            else:
                n=3*n+1;#print(int((n-1)/3),'-->',int(n))
            collatz.append(int(n))
        for i,b in enumerate(collatz):
            #print(b, num)
            if b<num and b!=0:
                #print('Pos:',i,'val:',int(b),'-->total links',len(collatz)-i)
                a[b]=len(collatz)-i

print(a.index(max(a)),max(a))