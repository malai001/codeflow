m = 11
n = 4
k = 

def binary(n):
	return bin(n)[2:]
	# if n >1 :
	# 	binary(n//2)
	# l.append(n%2)
	# return l
m = str(binary(m))
res = ''
for j in xrange(n):
	for i in m:
		if i=='0':
			res +='01'
		else:
			res +='10'  
	m = res
	res = ''
print m[k]
