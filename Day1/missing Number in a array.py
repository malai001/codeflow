for j in xrange(int(input())):
	a = map(int,raw_input().split(' '))
	n = max(a)
	s = n*(n+1)
	s = s/2
	# print s
	for i in a:
		s = s-i
	print s