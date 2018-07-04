M=999
palin=[]	
while M>=1:
	N=999
	while N>=1:
		Num=M*N
		if str(Num)==str(Num)[::-1]:
			#print(M,'*',N,'=',Num)
			palin.append(Num)
			break
		N=N-1
	M=M-1
print(max(palin))