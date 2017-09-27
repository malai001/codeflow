a = map(int,raw_input().split(' '))
n = len(a)
l = [1]*n
for i in xrange(1,n):
	for j in xrange(0,i):
		if a[i]>a[j] and l[i] <l[j]+1:
			l[i] = l[j]+1
m = -999
for i in l:
	if m<i:
		m = i
print m