s = 15
a = [4,3,7,5]
c_s = a[0]
st = 0
n = len(a)
for i in xrange(1,n+1):
	while( c_s > s and st < i-1):
		c_s = c_s - a[st]
		st+=1

	if c_s == s:
		print st,i-1
		break

	if i <n :
		c_s = c_s +a[i]
