from math import sqrt
triplets=[]
for x in range(1,333):
	for y in range(x,500):
		z=sqrt(x**2+y**2)
		if z%1==0:
			z=int(z)
			triplets.append((x,y,z))

print(triplets)
sum1=[(x,y,z) for (x,y,z) in triplets if x+y+z==1000]

print(sum1)
print(sum1[0][0]*sum1[0][1]*sum1[0][2])