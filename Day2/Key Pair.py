s = 5
a = [2,5,3,10,6]
b = [0]*len(a)
k = 0
for i in a:
	temp = s-i
	if temp>0 and temp not in b:
		b[k] = temp
		k+=1
	if temp in a:
		print i,temp
		break