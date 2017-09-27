for i in range(int(input())):	
	n = int(input())
	a= list(map(int,input().split()))
	i = -1
	for j in range(0,n):
		if a[j]<0:
			i+=1
			a[i],a[j] = a[j],a[i]
	
	p = i+1
	n1 = 0
	while n1<p and a[n1]<0 and p<n:
		a[n1],a[p] = a[p],a[n1]
		p+=1
		n1+=2
	for i in a:
		print(i,end=' ')
	print(end='')
	